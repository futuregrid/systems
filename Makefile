all:
	cd /tmp
	rm -rf /tmp/git-systems
	mkdir -p /tmp/git-systems
	cd /tmp/git-systems; git clone git://github.com/futuregrid/doc.git
	cd /tmp/git-systems/doc/doc; ls; make html
	cp -r /tmp/git-systems/doc/doc/build/html/* .
	git add .
	git commit -a -m "updating the github pages"
#	git commit -a _sources
#	git commit -a _static
	git push
	git checkout master
