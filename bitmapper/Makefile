all: install render

.PHONY: all

clean:
	@find . -type f -name "yarn.lock" -exec rm -rf "{}" +;
	@find . -type d -name "node_modules" -exec rm -rf "{}" +;

node_modules:
	@mkdir -p $@

install: node_modules package.json 
	@yarn install

render_modern:
	@yarn render:bibata-rainbow-modern

render_original:
	@yarn render:bibata-rainbow-original

render: render_modern render_original
