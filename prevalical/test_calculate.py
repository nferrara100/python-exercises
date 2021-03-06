from calculate import get_query_stats

# Pytest test suite for the calculations. All use example data.


def test_correct_count():
    stats = get_query_stats("reflects")
    assert stats["count"] == 1
    assert len(stats["examples"]) == 1


def test_correct_count_2():
    stats = get_query_stats("worst")
    assert stats["count"] == 4
    assert len(stats["examples"]) == 4
    assert len(stats["locations"]) == 3
    assert "doc1.txt" in stats["locations"]


def test_correct_count_3():
    stats = get_query_stats("that")
    assert stats["count"] == 503
    assert len(stats["examples"]) == 387


def test_multiple_word_query():
    stats = get_query_stats("Old State Capitol")
    assert stats["locations"] == ["doc1.txt"]


def test_simple_example_sentence():
    stats = get_query_stats("Thank")
    assert "[bold red]Thank[/bold red] you." in stats["examples"]


def test_long_example_sentence():
    stats = get_query_stats("biological")
    assert (
        "And we need to work together to obtain a bilateral agreement on [bold red]biological[/bold red] threat reduction."
        in stats["examples"]
    )


def test_word_end_of_sentence():
    stats = get_query_stats("kiev")
    assert (
        "We were in Ukraine, visiting a pathogen laboratory in [bold red]Kiev[/bold red]."
        in stats["examples"]
    )


def test_case_insensitive():
    stats = get_query_stats("DiFfIcUlT")
    assert "It will be [bold red]difficult[/bold red]." in stats["examples"]


def test_nonalphabetic_char():
    stats = get_query_stats("my family's")
    assert (
        "In many ways, then, [bold red]my family's[/bold red] life reflects some of the contradictions of Kenya, and indeed, the African continent as a whole."
        in stats["examples"]
    )


def test_start_of_sentence():
    stats = get_query_stats("Let me begin by saying thanks")
    assert (
        "[bold red]Let me begin by saying thanks[/bold red] to all you who've traveled, from far and wide, to brave the cold today."
        in stats["examples"]
    )
