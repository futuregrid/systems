all:
	cd /tmp
	rm -rf /tmp/git-systems
	mkdir -p /tmp/git-systems
	cd /tmp/git-systems; git clone git://github.com/futuregrid/doc.git
	cd /tmp/git-systems/doc/doc; ls; make html
	cp -r /tmp/git-systems/doc/doc/build/html/* .
	pwd
	ls
	git add .
	git add _sources
	git add _static
	git commit -a -m "updating the github pages"
	git push
	git checkout master
