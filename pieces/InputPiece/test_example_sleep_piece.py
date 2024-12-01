from domino.testing import piece_dry_run

def test_example_simple_piece():
    input_data = dict(
        search="Sample input"
    )
    output_data = piece_dry_run(
        "InputPiece",
        input_data,
    )

    assert output_data["message"] is not None
