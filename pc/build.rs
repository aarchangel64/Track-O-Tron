
fn main() {
    cxx_build::bridge("src/main.rs")
        .file("src/attitudeConv.cpp")
        .flag_if_supported("-std=c++20")
        .compile("pc");
}
