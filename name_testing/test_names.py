from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
  assert make_full_name("Matias", "VIllar") == "Villar; Matias"
  assert make_full_name("Jessica", "Johnson-Johnson") == "Johnson-Johnson; Jessica"
  assert make_full_name("Ja", "Je") == "Je; Ja"
  assert make_full_name("J  a", "J  e") == "J  e; J  a"
  assert make_full_name("", "") == "; "