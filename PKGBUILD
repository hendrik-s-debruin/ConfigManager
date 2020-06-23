url="https://github.com/hendrik-s-debruin/ConfigManager"
pkgname=ConfigManager
pkgver=0.0.0
pkgrel=1
pkgdesc="Dot file configuration management"
arch=('any')
depends=(python)
optdepends=(zsh)

package() {
	# TODO usually you should fetch code from the src directory, but since this
	# package is not published on AUR just assume the PKGBUILD file is in the
	# correct location relative to the rest of the code. That is, we can get to
	# cfgmgr by calling ../cfgmgr
	mkdir --parents $pkgdir/usr/local/bin
	cp ../cfgmgr $pkgdir/usr/local/bin

	mkdir --parents $pkgdir/usr/share/zsh/functions/Completion/Unix
	cp ../_cfgmgr $pkgdir/usr/share/zsh/functions/Completion/Unix
}
