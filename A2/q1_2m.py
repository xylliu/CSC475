Series {
    inSamples = 2048
    -> input: SoundFileSource { filename = "output.wav" }
    -> Windowing { size = 2048 }

    -> AutoCorrelation
    -> Peaker
    -> MaxArgMax

    -> Transposer
    -> selection: Selector { disable = 0 }

    -> sink: CsvSink { filename = "q1.2.1.csv" }
    + done = (input/hasData == false)
}
