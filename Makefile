.PHONY: book serve clean

book:
	cd book && uv run jupyter book build --html

serve:
	cd book && uv run jupyter book start

clean:
	cd book && uv run jupyter book clean --all --yes
