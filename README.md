# Python Rekor Monitor

Verify your software using trusted supply chains.

![Release status](https://github.com/JacksonQuu/Software-Supply-Chain-Security/actions/workflows/cd.yml/badge.svg)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/JacksonQuu/Software-Supply-Chain-Security/badge)](https://scorecard.dev/viewer/?uri=github.com/JacksonQuu/Software-Supply-Chain-Security)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/9753/badge)](https://bestpractices.coreinfrastructure.org/en/projects/9753)

## Description

This repository uses `Rekor API`, a tool that helps improve security in software supply chains by providing immutable records of software build metadata. This repository includes code that interacts with Rekor's API and verifies the consistency using transparency logs.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/JacksonQu/Software-Supply-Chain-Security-Assignment1.git
cd Software-Supply-Chain-Security-Assignment1/
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install cryptography requests
```

## Usage

- Fetch a checkpoint of Rekor transparency log.

```bash
python main.py -c
```

- Verify the artifact signature.

```bash
python main.py --inclusion {logIndex} --artifact {filepath}
```

- Verify merkle tree consistency.

```bash
python main.py --consistency --tree-id {treeID} --tree-size {treeSize} --root-hash {hash}
```

## Reference

- Fork from [mayank-ramnani/python-rekor-monitor-template](https://github.com/mayank-ramnani/python-rekor-monitor-template)

- [Rekor API Sepc](https://www.sigstore.dev/swagger/#/)
