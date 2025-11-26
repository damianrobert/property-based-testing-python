import json
from hypothesis import given
import hypothesis.strategies as st


# Strategii pentru structuri JSON valide (fără NaN/Inf deoarece JSON nu le suportă oficial)
json_scalars = st.one_of(st.integers(), st.floats(
    allow_nan=False, allow_infinity=False), st.text())
json_arrays = st.lists(st.deferred(lambda: json_values), max_size=10)
json_objects = st.dictionaries(
    st.text(), st.deferred(lambda: json_values), max_size=10)
json_values = st.one_of(json_scalars, json_arrays, json_objects, st.none())


@given(json_values)
def test_json_round_trip(v):
    data = json.dumps(v)  # serializare
    v2 = json.loads(data)  # deserializare
    assert v2 == v
