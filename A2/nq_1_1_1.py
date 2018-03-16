Series {
    Samples =p 2048
    -> input: SoundFileSource { filename = "qbh_examples.wav" }
    -> Window { size = 2048 }

    -> Spectrum
    -> PowerSpectrum { spectrumType = "magnitude" }

    -> Transposer
    -> max: MaxArgMax

    -> Transposer
    -> selection: Selector { disable = 0 }

    -> sink: CsvSink { filename = "q1.1.1.csv" }
    + done = (input/hasData == false)
}
