from hypothesis import given
import hypothesis.strategies as st
from dedup import unique_preserving_order


@given(st.lists(st.integers()))
def test_unique_preserves_first_occurrence_order(xs):
    ys = unique_preserving_order(xs)
    # 1) Elementele din ys apar și în xs
    assert all(y in xs for y in ys)
    # 2) Fără duplicate în ys
    assert len(ys) == len(set(ys))
    # 3) Ordinea apariției în xs se păstrează în ys
    # Pentru orice doi din ys, poziția în xs păstrează ordinea relativă
    for i in range(len(ys)):
        for j in range(i + 1, len(ys)):
            assert xs.index(ys[i]) < xs.index(ys[j])
