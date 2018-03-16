Series {
    inSamples = 2048
    -> input: SoundFileSource { filename = "qbh_examples.wav" }
    -> Windowing { size = 2048 }
    -> Fanout {

        -> Series {
            -> Spectrum
            -> PowerSpectrum { spectrumType = "magnitude" }
            -> Transposer
            -> max: MaxArgMax
            -> Transposer
            -> selection_1: Selector { disable = 0 }
        }
        -> Series {
            -> AutoCorrelation
            -> Peaker
            -> MaxArgMax
            -> Transposer
            -> selection_2: Selector { disable = 0 }
        }
    }
    -> summer: Sum
    -> sink: CsvSink { filename = "q1.3.csv" }
    + done = (input/hasData == false)
}
