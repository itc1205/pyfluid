.SILENT:

BLACK_FMT=python -m black

format:
	$(BLACK_FMT) src

format-diff:
	$(BLACK_FMT) src --diff
