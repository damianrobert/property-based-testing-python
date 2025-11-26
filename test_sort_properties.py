import pytest
from hypothesis import given, settings
import hypothesis.strategies as st


@given(st.lists(st.integers()))
def test_sort_is_idempotent(xs):
    assert sorted(sorted(xs)) == sorted(xs)


@given(st.lists(st.integers()))
def test_sort_preserves_length(xs):
    assert len(sorted(xs)) == len(xs)


@given(st.lists(st.integers()))
def test_sort_is_ordered(xs):
    ys = sorted(xs)
    assert all(ys[i] <= ys[i+1] for i in range(len(ys) - 1))


@given(st.lists(st.integers()), st.lists(st.integers()))
def test_sort_concat_equivalence(xs, ys):

    # sort(xs + ys) == merge(sort(xs), sort(ys)) – proprietate clasică
    sxy = sorted(xs + ys)
    sx, sy = sorted(xs), sorted(ys)
    # verificăm că interclasarea păstrează ordinea globală
    i = j = 0
    merged = []
    while i < len(sx) and j < len(sy):
        if sx[i] <= sy[j]:
            merged.append(sx[i])
            i += 1
        else:
            merged.append(sy[j])
            j += 1
    merged.extend(sx[i:])
    merged.extend(sy[j:])
    assert merged == sxy
