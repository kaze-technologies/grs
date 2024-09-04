# FloripaSat GRS: Ground Station of the FloripaSat Project (MORELLO CHERI BUILD)

## Installation

Building GUI application with HybridABI:

```
make gui
```

Building florisat-grs Commandline application without GUI dependencies and full CheriABI Pure Capabilities binary:

```
make cli
```


Check program is Purecap or Hybrid:

(Hybrid output)
```
floripasat-grs: ELF 64-bit LSB executable, ARM aarch64, A64, version 1 (FreeBSD), dynamically linked, interpreter /libexec/ld-elf.so.1, for FreeBSD 14.0 (1400094), FreeBSD-style, with debug_info, not stripped
```

(Cheri purecap output)
```
floripasat-grs-cli: ELF 64-bit LSB pie executable, ARM aarch64, C64, CheriABI, version 1 (SYSV), dynamically linked, interpreter /libexec/ld-elf.so.1, for FreeBSD 14.0 (1400094), FreeBSD-style, with debug_info, not stripped
```

## Resources

* FloripaSat project homepage: [http://www.floripasat.ufsc.br/](http://www.floripasat.ufsc.br/)
* FloripaSat project source code: [https://github.com/floripasat](https://github.com/floripasat)
* GRS documentation: [https://github.com/floripasat/grs/wiki](https://github.com/floripasat/grs/wiki)

