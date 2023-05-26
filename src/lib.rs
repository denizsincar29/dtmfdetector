use pyo3::prelude::*;
use dtmf::{decoder::{Decoder, ToneChange}, enums::{State, Tone}};

struct Tones {
	tone: char,
	tones: String,
}

impl ToneChange for Tones {
	fn tone_change(&mut self, tone: Tone, state: State) {
		match state{
			State::On => {self.tone=tone.as_char(); self.tones.push(self.tone);}
			State::Off => {self.tone='n'}
		}
	}
}


#[pyclass]
struct Detector {
	#[pyo3(get, set)]
	pub samplerate: u32,
	decoder: Decoder<Tones>
}

#[pymethods]
impl Detector {
#[new]
fn new(sr: u32) -> Self {
	Self{samplerate: sr, decoder: Decoder::new(sr, Tones { tone: 'n', tones: "".to_string() })}
}
#[getter]
fn last_tone(&self) -> char{self.decoder.tone_change.tone}
#[getter]
fn tones(&self) -> String {self.decoder.tone_change.tones.clone()}


fn decode(&mut self, data: Vec<f32>) -> PyResult<()> {
	self.decoder.process(&data);
	Ok(())
}
}

#[pymodule]
fn dtmfdetector(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Detector>()?;    Ok(())
}
