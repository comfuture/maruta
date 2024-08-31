use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python function that prints a personalized greeting.
#[pyfunction]
#[pyo3(signature = (name=None))]
fn greet(name: Option<String>) -> PyResult<String> {
    let name = name.unwrap_or_else(|| "World".to_string());
    Ok(format!("Hello, {}!", name))
}

/// A Python module implemented in Rust.
#[pymodule]
fn maruta(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(greet, m)?)?;
    Ok(())
}
