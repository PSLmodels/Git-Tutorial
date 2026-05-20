.PHONY: book

book:
	cd book && uv run jupyter book clean --all --yes && uv run jupyter book build --all
