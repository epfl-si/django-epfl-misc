# Changelog

## v2.2.0 / 2025-12-09

### Features

- Add Python 3.14 support (#95).

### Fixes

- Add Django as dependency (#97).

### Misc

- Update isort to 7.0.0 (#96).
- Update flake8 to 7.3.0 (#94).
- Update black to 25.11.0 (#93).

## v2.1.0 / 2025-12-03

### Fixes

- Fix files included with pdm build (#83).

### Misc

- Add html report (#90).
- Launch pytest from VS Code (#91).
- Init Makefile (#84).
- Add targets setup, venv, installdeps and cleanall (#88).
- Add targets clean, lint and test (#87).
- Improve CONTRIBUTING (#89).
- Run linter only on latest Python (#86).
- Refactor requirements (#85).
- Update codecov/codecov-action to v5 (#82).
- Update actions/setup-python to v6 (#81).
- Update actions/checkout to v5 (#80).

## v2.0.1 / 2025-07-21

### Misc

- Modernize packaging (#78).
- Simplify tox tests (#77).
- Remove license classifier (#76).

## v2.0.0 / 2025-07-17

### Backwards Incompatible Changes

- Drop Python 3.6 support (#68).

### Features

- Add Python 3.13 support (#70).
- Add Django 5.2 support (#69).

### Misc

- Add VS Code settings (#64).
- Add VS Code recommended extensions (#63).
- Update actions/setup-python to v5 (#67).
- Update actions/checkout to v4 (#65).
- Update codecov/codecov-action to v4 (#66).
- Fix Markdown heading style (#71).

## v1.1.0 / 2023-12-21

### Features

- Add Python 3.11 support (#52).
- Add Python 3.12 support (#57).
- Add Django 4.2 support (#54).

### Fixes

- Fix GitHub Actions badge (#56).

### Misc

- Update codecov-action to v3 (#59).

## v1.0.0 / 2022-10-10

### Backwards Incompatible Changes

- Drop Python 2.7 support (#29).
- Drop Python 3.5 support (#38).
- Drop Django 1.11 support (#29).

### Features

- Add Python 3.10 support (#46).

### Misc

- Lint via tox (#48).
- Update pytest ecosystem (#44).
- Update flake8 from 3.9.2 to 5.0.4 (#42).
- Update checkout action from v2 to v3 (#34).
- Update setup-python action from v2 to v4 (#36).

## v0.1.0 / 2022-10-04

### Features

- Add Django 3.2 support (#27).

### Fixes

- Fix release workflow (#12).

### Misc

- Update flake8 from 3.8.4 to 3.9.2 (#13, #15, #21).
- Update isort from 5.7.0 to 5.8.0 (#17).
- Update pytest-cov from 2.11.1 to 2.12.0 (#23).
- Update black from 20.8b1 to 22.8.0 (#19, #27).
- Update codecov-action from v1 to v2 (#25).
- Pin importlib-metadata to 2.1.3 (#31).

## v0.0.2 / 2021-02-22

### Features

- Add decorator `superuser_required_or_403()` (#9).
- Add Python 3.9 support (#7).
  
### Misc

- Add release workflow to PyPI with GitHub Actions.
- Add project urls in `setup.py` metadata (#10).
- Tweak black and isort config (#5, #6, #8).

## v0.0.1 / 2021-02-08

- First version, released on an unsuspecting world.
