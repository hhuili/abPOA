import telox_pyabpoa as pyabpoa


def main():
    ascii_aligner = pyabpoa.msa_aligner(is_ascii=True)
    ascii_result = ascii_aligner.msa(
        ["A@#Z", "A@#Z"],
        out_cons=True,
        out_msa=False,
    )
    assert ascii_result.cons_seq == ["A@#Z"]

    dna_aligner = pyabpoa.msa_aligner()
    dna_result = dna_aligner.msa(
        ["ACGT", "ACGT"],
        out_cons=True,
        out_msa=False,
    )
    assert dna_result.cons_seq == ["ACGT"]


if __name__ == "__main__":
    main()
