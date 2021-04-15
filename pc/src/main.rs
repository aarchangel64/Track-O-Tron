// TODO: refactor using https://github.com/berkowski/mio-serial/blob/v4.0_serialstream/examples/read_serialport.rs

extern crate mio;
extern crate mio_serial;

use std::io::Read;
use std::str;
use std::{io, time::Duration};

use mio::Token;
use mio_serial::{DataBits, FlowControl, Parity, SerialPortSettings, SerialStream, StopBits};

const SERIAL_TOKEN: Token = Token(0);

#[cfg(unix)]
const DEFAULT_TTY: &str = "/dev/ttyACM0";
#[cfg(windows)]
const DEFAULT_TTY: &str = "COM1";

#[cxx::bridge]
mod ffi {
    extern "Rust" {}

    unsafe extern "C++" {
        include!("pc/include/attitudeConv.hpp");

        type AttitudeConverter;

        fn new_converter() -> UniquePtr<AttitudeConverter>;
    }
}

fn main() {
    // let est = ffi::new_converter();

    const SERIAL_SETTINGS: SerialPortSettings = SerialPortSettings {
        baud_rate: 115200,
        data_bits: DataBits::Eight,
        flow_control: FlowControl::Software,
        parity: Parity::None,
        stop_bits: StopBits::One,
        timeout: Duration::from_millis(1),
    };

    let mut rx = mio_serial::SerialStream::open(&DEFAULT_TTY, &SERIAL_SETTINGS).unwrap();
}
