---
company: Varex
excalidraw-export-embed-scene: false
excalidraw-export-transparent: false
excalidraw-export-dark: true
excalidraw-export-pngscale: 1
excalidraw-export-padding: 10
excalidraw-plugin: parsed
tags:
  - excalidraw
  - archive_deprecated/Varex/logging/tests
---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data
## Text Elements
testPartialLoggerName ^dundOPfu

newSeverityMap ^K5CbKVVu

createTestLogSettingsFile() ^MMKUZPJO

settings ^NfA0Ej2x

logger ^mHDNHQD7

create_logger() ^zkVTpJFb

This creates a back-end settings file that we then reference with the settings object ^7c2aE06k

Create/initialize settings object ^d0HNUJvC

settings->getMaxLogFileSize is 0
(might be 00?) ^OennoDKb

settings->getNumLogFiles() is 0 ^tJUzSv9J

settings->getReload() is 2 ^zYjyhOD0

settings file for change time? ^6amNRWos

compare settings->getFormat() to a string? ^85jkYror

settings->getSeverity() ^uyzHPouB

This is probably where the test isn't working like we think. I'm not sure what Jim thinks is going on here. ^z31uPQHF

msg2(loggerName +  "-info message") ^372g7Uqx

msg1(loggerName + "-warning message") ^F2i2QkxO

VLOG_WARN(logger, "{}", msg1) ^NaGV4XrV

VLOG_INFO(logger, "{}", msg2) ^KRkHEYjF

get()->flush() ^jUPMZh8R

I don't think this process truly is testing for a partial wildcard. It's passing, but I don't see how there's a "partial" amount of anything going on here.
 ^x39R4zoF

testLoggerName = "SettingsFileTests.SettingsFilePartialWildcard" ^pEcL2V22

testPartialLoggerName = "SettingsFileTests.*" ^6i6EdiOj

logger = Vlog::initLogging(settings) ^O3yj2PGC

logSettingsFileSettingsPartialWildcardTest ^Mq8BjPAA

settings = std::make_shared<VlogSettingsFile>(logOutputFile, logSettingsFilePartialWildcardTest) ^jsgQFWgE

logOutputFile
string (path to logfile name) ^jCFWwoHH

ASSERTIONS: ^VfWoyjrj

couldn't open  ^2vLyx53x

severityMap
testPartialLoggerName = warn
* = info ^ZaQxzGja

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebTiANho6IIR9BA4oZm4AbXAwUDAi6HhxdEDsKI5lYOSiyEYWdi40AE4AdgAWfmLG1k4AOU4xbh4ABgBWBLGeTs6ARgBmHshC

DmIsbghcMbriwmYAEVSoBGJuADMCMJWIEi2ADgAFAFUAcXaAK1J2gFFD1g8ADqAEk3vgABrtADCVFuF0I+HwAGVYLUJIIPHsBFBSGwANYIIEkdTcea3Zi4gkIVEwdHoTH3W54vySDjhbJoMa3NhwXDYNQwMljbn5SDWGplUX1CCYbiLMaLbQPRbteadB5dcaTPhiiBCtDq9oJbTzB48HiteYJBJm80PClUwnQtj4NikLYAYnmCB9PuxEE0/PxyhZ

6xdbo9Elx1mYfMCmQDFBJklGCVa2kWi3mY3mPCWi06CodeskCEIymk3Am820EzGrWzIva7TG6aWFIQZzJE0WrU6ataPGWetDwjgIOInNQOQAuvDyOlJ1tDgAJNjI7AALQAagB5CEAfUIrQAjm8eE9mHuHjB8QGw8R2cxp4UZbBEPKxQBfW6aYTrL8wTpJk055PUBRivs5wSAA0hM0KaLBO47kI2LFB+ZTQFgUAQFBv5QW+Mr3BIO64IQEzOAAsjA

kifA8hykBQiwXKeAw8PiAAyuwrBhpRbLgpB4lQ+FivOepCHAxC4KcMGoPMaoPAknT1laXStLcRAcPeaAcEISKaWw2CEnJVz4GE+QEUURElJ+0Y4QGfTNNwrYjjKTmDMMZQJIsDwTK0fkPBpeprBscoSLg8wBgcxzBLJlzXAgtwkeg8GIchqEBgiSK0vSECMucjp4oSxLEKSaC6jKlLFTSaJYQVD7CJWz7TuSeq8vygrCtKxQSvSPWQOFqCLFM2gD

uqYwamMmrjAktwGvJGoZo26adAkraTQp3R6tV1IRu6Xp+r6SB/sGY5COGroHdG5AcHGgkZLhtzJmVqaGsp2htjwEy3GWFZVhV21VV2cnzEsEztA81oQ7c50TlOuTiTKFyLggy4SGuG7bvuR4nuel7Xre97MgBT4ctwekGXq/4XcQQFpI9YFI8UknSfFhqKcpqlbcFMpaTpqCU/ghnGd2aBmTceoXJwUDIoQRhlOM8IywAYrg+iIgtbkYQ5EjshQy

III0gpUbgcAPpQAAquvoPrhvG7Apvm7cpyYFAACCRDKC06BiJkTCOUwUDmAQnsVj7EAa8QxC1LceiZOR7KkOj6DPO8Xw/P8gKguCUKwgG7oVmsBDW27Wx20bTAm2bAa4EIUBsAASuE8tlLiQhJXqWkIKu5aVrhhrxJZPQ2ZhAlCWwcJ6h5Pu+ZDtwz0MHAjIaAUdAskw/SF6ybBFPDRUcJxi6gEud8RckQGRFHUbR9GMcxrHsVxPFS4iKJ1VsDVF

dSpXlfJ3+ElyvVV0TI9QsmauTLkPI+QClgN1W4fUpS3CGhDCYpoEhQ2mJqCYRZ/LzTJAOE0nR8zWlVHMHgDwVIAIQPtKM6BvTHX9KdYy51LqRi2DGO68ZHpJhTNwVoJoRRCOEUI4cv0+4A3ku0bQQ5CxZiCgkCY9YZjawECDbgA5IabzEaOFk8MmYLnVmjC+mNNy7gPMeM8F4rw3jvI1WmLVuBEUgGPCqP4/yk3piBLIiNbisxksfBSdp5hKJtCo

zSawBZCxFiZBK5kz7FEpIJKAAAhUKaxlBOKghgYCj0U4QDTh8b4fwASEGBGCSEMIp4QQgMoGug9WiNKac0ppRZKrIyMkIaczhpFzCUX0pYfliEIGcNadxeoMjEDSesDJWSampG8fk6EKSACamgABSPdMCHFaIeAY+IoA8GwJoeY2BFgDHQrU+p8kZEtLueaVoW8anS2wF07gzg4hDjNIsChEMiwtk6I2EZITxl81CFAF0+gNYyDOE8NgawB6C30s

LHaURSAewnhQMsuA5LRImesd2mLsUX0EsJAMcB4WgVyFBcCEEBpFDGFBZmRRaX1AEZ9ERnKdEQTAKM6Rsiiy+QEUokUw4mViWHvkUe/EIqYsDk0TgGisxPN6EwfoHAl4r1QF8n5AUlHJR3kNbYnQD6xQQOzE+iVkoXx4PgSQVFPjuxVgkDgIJMBjHWXuCY8A3ifE4sTV+OUP4YhAYVVFNVf5vX/uG6kQDP6hvsRAl83ABoQA6rAhaOZU2IJTcg6s

7Q0HWkwdNAtRY5p6kzaqNB/ZCzzEeQ8Sasx2jUNoYdRhJ1qZnUfK2m6sZuGJmenwtogjOUiLBuI/6iKFIyOHIKhR+YRptWBoEngXQbR5hGrDPRk4DFS1Rvk0x2MLF42sYTOxJMHGQNQM42yitQXFBpoBXJVK0Bzj8VJAJoNFJQ1CdMWYETtIU2RTE4+p9HTJOmY4aocyZQLLyRfdZTwHj0HokIKiKznBTmhDuZwFw4CaF+DwN4ly6nmwqrxCALy3

loCVO0C0LYLRTCHGqXMwKEj3sgJMyDsy0A3rg5kJZqyNlbJ2Xsg5RyTlnIuRR0jZJbl3OaQx8tzzOnTk+fmFUvyuiqnUosYFEwOMQHwOCyF0LZJwoRUBqmVU0UYuEsSqzKLYMEqJSEElcrbgUoRWBGlUEwD0v80y3irKijstHWOpdEFp0CvkQIhdNZxX1FnJK6yepXHlAQJUHNC81XOUNCKXmqqFUaq8mSBSFDHk4MK6sQ1AkJimqPqZK1IUL7LL

WZs1c2zdn7MOcc055yspvzjSGrE1DI1kmocNhkCaL1JunKm9NXV8vZuqP1PNaB1pKiLdaEtOCRrVf1GSRY61MwjRtFMaa6YBEtqunQiADCjoBiDCw7tt2OG3XugmJ6eoXp/0LHEBSkxFTDgmEpEJqipASKndO9MPyJj5jbMd5S7S1HHwXf2DoIOt3jh3b4vdRiD3rjMTjSx+MbFE3sesRxvHsnpcWIZx9dNn0+NfYRPzdwL5USorBF4W4nievQi4

mV6BXa4XwrxZxqwL5X0ojROiDEmIsTYhxbigvb3jzJeLtnPKOdbFtfax1zrXXus9d6uAvr/Vq/S9sOVWuIKS91xIbALx5gwAQBMTQHAxgvCBC8T4FAQTYDgFuFZYxYJW+FzbzXEFvxiXfWzQJnMVINh5gBqJwGu5GVieLRKKXILvkj6L+V6rhTmhy8VzVZQwaFgSDwdaCkDVhQEkkZKh84qgea+fLYXOed84F/CIbwbpujZjSVIdvBJtD/yjNsBT

U2RXsi5ARbcDlsINW0gvUQ0MGCPrBQ3TSPm0VoIeqU05pLTWltA8e0N32ESAe8dJ7XbSY9pFx9/t32ZS/ajdmIhX0VWQD+n7lGCBkSXUXemmjrWUgbGx0klx1fWZUo33RMSJyPVxisQJlsQDRlEfGpyRWswfU8WZ13RlH8QtSCSUmTzUkBTT0cxAya3iWVkyDlgVlGFTWlkyDVg1nwC1hdhtggGwECACWtkpE4jYGUENhkAyWYBVkRAQAAAoABKC

2CgUuRFfgwQ04YQqAUQ8Q81YOaoaQ2QxQgMUXMOb2LYP2U4D0cvYOdwMwiOKOGODtGUeOKINYJgQTdrETbrcTPrKTAuUgIuDgEuPggQkITQ8IbQsQiQ/Q5QQw4IYwhBeuJuFuFgtAduBJSAbuXuSdOTHgPPaVOyDLLLdfYvPLbVK0cvdVSvbgIKDUaGBYRvXedAXAdoBrdvegyWLvCQB4IEeYCEAARSMBSRxQoBeHWTD2cFXHwCMAoAuBfmRkHzp

GARHxswjXH0X3yidFqmWPjVWOKHAXn2TSgXahgSW3khFDX0lFzU334U1DrFBzbH8naEaSvxAMgEzV7CVAbGITVAwQbTrRv2unoSOiYU7Re2fze17S4QegHR+3HzrwzCzBzDzALCLGmgnSALQFGltCWlzDCXhzVE7ECWmGO0oV7E2LhjgJnAQJRgJ2QKxnMTQLJzPSwIONJlwJvTpwZ0IIZhfRnG1xqRSggFgkWFXAGLeE4lCk0GUFaFhGYE6EwCM

GhFgmdnZ2t1JUnjwhjwl3Z2FO0M4iMA4EwE0B4CMAhCokkFIHeEwF+ConaFwDlF4iFyKKjy1Lt3qAd2FNaCICYAoG8AGEIGhB4GRHmBVhWR4Hdk0AGAhAj1dM1JEh1MFO6PQFXEPA4FXDgASEOE6AGHWSBE+GhD3HWUwBeAuGcA4BVjjKwgTO1PqCsk9L1IvklMtj3DeBIEtgSGYGICEEPFwEbkICEAmEIEWEIGrI13dKTPtybK2EIAGM4kwFIEO

FwFPEtjeFgmhHoB3DGCBFWXxAuHoHHNlWj3rN1J12FIGAuHdjGF+E+B4CdPVMLwclEiS3j0/TJCT25nUhoN0gzz5izw73iQKLSyfLLiqPKIEWUyK2qNK0NHGEeQbFmH/zuFqwigeHaPNUAq6Ogi2EvOvNvPvMGyDV2JG1ATWJ/gRMnxIuHzIvZNZFwM2OX0zUuL1BzROJlCGhzALUzA1AhnGDWlchLBlE+MBTGlzD+JbBzBUneK2Jqhf3u1BOcIf

Sf1pnks4U+x4UHVen4Vo2QsAMkX/R2jAPkmUj8mO2+RgP0Tx2RiQJXBQKZNJ1PUwMpzJmOLwKcwINpi8UZmspZg/TIM/JT2/K7kiVoMz1Fk6MyMoxlmYMVjYNVnVk1nlF4LLgxD0KkOUNUM/nSoMJMJwnsIsMegDhsJDnwAKokEcNjj1FcMTg8Ivl6P6KGJGOIDGImNgimJmLmIWOKELn8BCNSoZByriNrmSOblYDSNQAyIAx7ihzyOAoL1dIqCq

GuPAsVQqk2lWpK2Xir2eIVB8n1W3ibwilaAwotTAxay2EPBBGcBSTTMtnwDgCgB3BeIeAVMPA+WIEtiIvfmoun32JxHWO0sNCoryi/ln3oqvQWzOJXwuJW2uPYuKCGn7BHVB1bDNFbHNCgo+LJHNFrHh2mCWiWnBiBLu3vzBJlGexDFe1v1fz7VhI/2KC/w0QWBkUBQwVBzzCtHWj0tmrQChnkwU2aWJLklwQ6HVHHV0RxwRngMMSXAvgGCoj3BV

gQDmPdkPBGnNLgEWCeHmCgGIE6HwBcs5Np2F3p1POpl5O8R82nPPIvlFPFMlOlNlPlMVOVNVKPJaNtynMbNtq2BST3FwGhAhFgigBWU6E0CMCgHmHWUVoGNrz3FXA9rdMTPNptqFIvkbjGEbnmDYCBASE0BBEtmwDIGhAGAoHmEwC3AoEPOdPV2PMnNTp9vTq2CEE4nzLYBSQmCoi3BgAtMWHxBSX0HdieFaAuCFFro1K9sbtS19okD3EWBgDvKe

DeGhCTqLxfKKAQNIMTzNC5iUivxVB/PcroLiQsiKAbMKKwiL02o/M3Wnly08m2rJERIoQHAOuIlQpaPdlOqwqiuFPnsXsvBXu+qmz+tooBooqBon1Hx2NBpn2wLnwYugU6hhqzSuLW1uLaFGkmh+SWAbBGkaKP0ND8jGDrDr0mjqKCmJpgfkrJqUsgEptYWIDUrf3pt4SgeIVrGwUxIMpkrCECWzGNBVEq0supLfXxzltwsVuVtVvVomE1u1t1v1

sNovSpyvTxQpstp8plokn8p3ooNB3+MPpCsA1/PwKyIAsisYNllblYOsc4KSpoxSrULdGUGUCYFQAAF5UAdxXHkBkA1g1AdD/BlA5CwhJCDClDmQrY+DXH3HSAvGfG/GAmOAgmxCQmwmhrmAom0t8qvYI5LDir770VSryr0BKr6H+CZZark4L4rqbq7qHqnqXq3qPqvqeRAi+r8AsqJA4mPHvHfGxD/HAmoi3GMlMmIm4icmZQ64G4xrbH0jSAO5

pqcisSbl8jz6R4QLFrMtlqqr3IH6fZObD8DmK9YL5IrRWgZhJoTn9hP7th3YHziI29MKrGLqJBRyhA0k1AKAjBsBmBSBfhCA4BMBTwIQEAIRG4QGp8wbyKx8oHNjdpAEYX4G6K5sbiZQmL4FWLSiEbBoysGwZE8xbQtolIhwsbDsKp1QHgxpFFHkC0GxWx+wSa21HtmEqbISaboBWGvt2G/4LQTQrn8wfI8GcxiweHEVFFMxKFzR2hVQVR1o6Nhb

qwwYdtATJbYDpaaTZbjEpGlaVary5GFGda9aDajar0uTTaeSvKiDqU06UyIBkQVZYJLZTx9AKBPhmA6l6AHgBgHgUkhAVYFbV6J7I9ayPSZ7m6JAjB8QdxLY4B1kVZNA17nyY849dGE8v1glCwr9cwUcjNQqzGPKLGIrT6EB5q+JXTr7imS84LOhU1F5znjsmxNRGkmijVcB3YjAf63mHWY242E2k3oXfrYXEltjxtyMYHQHR3IBDikHTiUHmK4a

MGOKysRoxo5W2wVQlgugZKFphWMwQkVQ1Q60r9GwIckWaEoSQT21H8ITVLr3uW6beWtK/4FI0FIY8webcjAZlWOYG0fl8xbnIAqStXxGbL6S9WZHDWNaIQtaTXlHzW3KNHPKn0+SWdtWM33yOZs2NQASId+Ywr/zS2c8GCpYYqFneB4qODEruDkrcmBr1DwiEBDw+nSBEiwEYnGOwiAlWP0mmAOP3w8nw5Cr/ZrDinbDQ58mtgKmAwar3DamthPn

vmoBfn/nAXgXQXwXIWAigj+q1CePTg+O3GBPpnepRrUi24lmorsjeb1mK2XSsIlrssa3yjiWG3Dmai+aFQpgz9NjQpmjthfge2y3rUthENkNUN0NMNmBsNcN8NCNiMB9iK4H/rZLIG32QaVjwGIA53IbkGM1sWZncXUBU0hoFQlRj3qWtQRR4d8FDQflOhtB1pLQf0ZWd2WW79FK72OWH2uX1L38+Wo1ETTsUSF05EMTSw7Oaw6x8Gs0Ww2xKijL

Akwc5hGk+xRGwPaTbKMZ7KScT0MCKdVHXLXwTaiizbNmLabX0Pram6HWez1g9wngLg0JQ2q3U3p788o30B9cHUnUXU3UPUvUfU/U2SFqayp7z702SC9Gs2DGgrqCTH09zGjNLGy2HO66RcHIb78sy9XPH6tU8w6NsErn/P7ncAqzW8zUzrO8cKJAHviAnuXvh3UucvL2J3oG4XYHsuw0EGIa3LGLoal30GN9V2aMQkxolEWwAoS1Zp6v5J5ExpV0

fIbRhwc383L3aHuv2WmGWHn3NL4SoHZhBFGwC0JXgC/2LjwYlJlJgPalt0tudXCdGT9v0Dydz1wa1HkO/zUOmcbvfLIBt64euYEeDtCOi2T7SPsLIB2CbGJqlZyOaOuCeCGO1DThKQnhkkrB8BgmmABgjFMq+D0+oBM+SmCBc/SB8/0g8q3Yyn+CirxPTnJOyrpOKqSAnC5PqmFP8kIuUMHg0MMMsMcM8MCMiNdOumemseM+s/y/+PK+C+ki5nLP

uApqTGZqf37PLvI3HOOFsf8efZ6383G2n60AC0vjGxvp22BIngQuo+/6L52hsAeBcBfg2wwfKMljWfeex3AbMup2p9pIzAMsN/1naIN8uC7Qrqvhxbw1Su62bVNNEl5VoSWxzPdmuwzAzAFgUwddFflXSdcb2bLcEr1zYTAkn2MJF9ob35ZLBtAxoAKCEhrA+RiEGoc3nBVTT8NQYjYQFPaEVCbdiCxQOkpI124u9j0bvVkkh2nAocGGWjfkiFi9

IXxncrud3J7m9y+5/cgeYPKHnDxvcIeJ5KHq+Sw4BVd6lBVPEjyI7FA3QJHS1GRw6RMFKOCfawVAAcZ0cnGqfLYJbEkAHBUAhncIKgFwAAAdDgJTVcDrBUA4TWIswH8HZQEAk1SQDJFQAUAoh6gDIP4MCAXAmAGQMQHELUCSBohCAfwaEKkKoA7AnwXZoX0Y5uCPBXg5gD4NQCBDJkIQrJifFkLRDYh8QnIRwFQApC0h21TIeoByH1DJmVQooSUO

cZ19ggFwBmg0CDilNW+IuXkJ3wTjd9cUPvJfJ02LjdM+C5QqoZUOqG1Dgh+Qgwo0OCDNCoAcQhIWWHaGdCEwGQ5ML0MSH9CwhhQzQMUMqAjUl+41MoOdT5juFVmkiWsBszAAX1tm2grUjj1QAq9NqXnC5laAoRZhcBh1QLrgAGK39LB0fR3L7Bdxu4PcXuH3H7gDxB4Q8YeFnjzwDDs8NiWXLYMQDYAwoQBuXMAW5ShqLsiuvUErmV1qJXNPoAHO

YLtjzDy8lgUrZVOdiwRXYKWmvR9nQx6669H2A3Nhq+yjSQw6wteQcCKDmBytGwzAi4k12zAhJpoyNTBNdmW5foy0ykBSAdlA68CY+O3dAIegcoHd3e7/HAhazO53pp6gYKQRh3A5+VM2H5YJL+nCQmCI+4VbPCiKipJJ0U3GaDDTnmTM5PCwmTrKJh6wSZ+s0mbJLJknYqZXk82QzFxnSQRjr02SfjFAHySP9n+r/BIGDxA7XIUcMfVTCmkMzGZK

QpmNQOZkpSIoJBWxZJISnsxuZTBnGFzF2JxQ9iIAXmaQb5h5QBZGUEEZlGABCxgB5RUwVdHWmVEDg+wqiIoKMkmiZgwY9YOohgmtACJEsm9DHpPTJSgjV0Q4CEec3ByNpa8EOALh2yhZU9GsoXd5qlDFISkpS6wGUnKQoAKklSKpNUosRS7EixsZI//iO1RagD+e82ArucTQbQCV2iNYUNxTISmUfIrYX5LyMhifIzQF2RpBpi6B4CFKt7HXtTRI

HSjyBn+cfEFFm4bxsw2YetgIgOz6Up0SkDkU0hzACJVQwrS3hxNPbjAOwGrKyjowg4CDj6nvE7oOMZzeVpBW9WHt6Kvx0Cwk3KMwYWzEnEcgxnwsdhBhzGZJIxsGaMfLWkYGs1asHeDkozNYyZrki+asRmPeSkNpoKkKGPWnGDHYBw30LMesHDG6S8xUY9DvkgaqDFhioxcYpMWmKzF5iJGa5NIjBj9hpom0bTP0goxUZukpDQ/hDABJqgFQRYDd

HWJMwGAzMsKFsYONDF2ZJ4DmAMc5mICdiyp3Y+utUmKDDj3Ro4ulM6QnF6CIIM46ifWFolLAJojE50qMlYk6jGkHEtCcKwPFgBksW/L7jvwkD8DKmM8YUEf087nMEc6UnAQdjvECR2mIUF5jTysF08rRe3YQSyWcrJcfqX/EkeO0opgTLps2I4tBIgGwSWKxXGAayMBhNdNQcrFsBjS/bv1igmaLivEALQdAlEF/BUHb1FFctPQmgWGRKNIl3ZyJ

BvSiQiy+imggOa0c/JqDmDqjew0iLMHh1inrRVolvLoG2DrQiNBJYjbbpBwql0Uve4g5Ya6Ou5W07Wd3Q6RAEPAqxnAW4TOlVLeAcB6A5ZQ4IeGUBRAdwAwT4EnXDZpt2pno7DlIkMFflEeXw0xmpLMFo87+ccLpA3H0DLkogMGPgajBfwO5L2XoHgCkgtkWy1c2UQ2nfnhwOz94tdYIukFoaBRQc9WDegCNuAuysI0IDQhkgUAjNs+8sDJPcIKF

DCXhR40ChMIYCHN5QPI/fpCMuZ1pswUMK/hFBeDIjNJUuCkWMFXADBxi9AENoGgunASYGHPRFtsWnYQTaRUEjFj1SF5MjxQLIuAVcxpYqQkBvI6aEqFXTPEIYDYTGhe22Ja9iJhAyUf1x5bIzGa4+OeESz1SbFmJFvA0dwE2zw54Kpoh3uaMQK0z1ZkEhmZJLdG3dt+HMrmTzL5nuwBZQs5wCLLFm4AJZUsrQRORTq6DN6b5AwfDyoJh9VJbY8wR

pNp7VibB8fajg4No4p8hOjHf2cxyDmpNg4BAVuOHIOGRzY55AFQnwSgUBIYFagEOQrEQVxFHhzw2OaYRmFGYEA4w+VM3zr4NwAJxQeTknBThtjeqawyfhAAwWnAsFcCogLgv2H4LkFrwlIu8OfGqz1+azP4dHPjIeZ9+8oF4heJP7yR8aMrfsHby2kRQdw2cgBWiM5nczeZYwfmYLOFmizxZksokXsTZ7XSEW5I0ijSLy70iYJqDF6cyLelwC8wV

+ZUDMBeptgxgZ/CHMxStBjRhGiodMLaDXSETxRJEzlmRKnlwkUZb7agXKxrBrQMEKkOjD6FGSLy7OtYNOcaDlbvtWwa6YFIi2MqA41Q30esJSS3kB8d5oktsQ6O94o8pJtrYSfLI/kh81I9YI+r/M1nBjwMYYnSYbM4wGS85BcouSXPTHUZUAzgUhkpC0yuTMBQSarBWLIzyQPJUyPpXpOKAFjnexOE6U5SO7ZJkpKaU0DgjPZpzyZgUa0JZKWUS

8Xi4wRSB0EbQH1cpDY/KU2MKmWY6ZOIDsa5gHEfKMAfYmqT8r3lDiWxx86cX5nHFBZmp9QUZHEsXSJLySKSgpc6UyXo1NsuSrxWtAKUTSpp3sqVECK2DOdSioIs0AdmP6E9oR60TGptPJ6+N1FB03ORIF+A9wVYjqKIECB3CkA9wnK3uI3BeC/ABgoyvgZ/3Llc9K5limitYrpGPTMWTcqAa9IQn4tV4olY0Iol3qbxswvIuiaaBeJWgJoiiG3qE

u17jyEZ72fXtEpnlQN4cTXWYMOBmgJL8w6oonp9CUXXMFgBaOvDxKCgjRLskwHgZUvmkMKmZtSxmfUqPlsyT5DKkXJxENLGlTS5pS0taTeC2l7SjpaWZD1xX2sOZUAdZC8CMDIh6ArQdZCmzLhezZJXonDp/OMGqzkexbVHhYNPjiKr6e/U5rW14A2hZFhPIsEOA1CFhqVR1FojuFjkxQnxWsl8dABzV5qC1Ra86TXLS6kiLFt0kVWiwekNyl8sq

2GiL1XWyhWCCoeIAOFl7ZhZgISTVR9Dox0Za8vxTGUJR/57QxRRqimipWIGk0LgL619UN3lA+R4gUMS/lNw36GVl0ItJsMK1tB+qmlFo3eTUo5LqMmZDS/3mBogBB95JrSqtSpLVmdL61Gi2PrFTsaJ9QFyfejhArUI8LmAzgAAHzuMoAAwIQPoB0IyFggzARQqgA8HdVZ2XHIjVkzI0UaqNNGsQnRvCCMbmNNfD2CQsKaN8islCkhbJzjhd96FF

8JlauBZXuw2VHKrlQnQQC8r+VgqlYXp3WGMdiNnG81Nxto2yEGNChJjVUJY3bALOgixZsszX4/Cp0Q8aaZfQJW7MXOLa8opaA85nM5FLkhSJqGhgZyB1TzfYHtN/phcMQQgQgDuFghPBnAFANgIcHmDMABVibE0usgGCHATFViq6b/yjRVyaos6nLjYulWNzGRcqxxQqu3WrwZuKqmsFfiYw1g7emaK7GJR+TA5AUd9LnqPIIEPr72T601WQOnmQ

Ama2JWYHuttV0Z7V6Sjfk6p+LoT4p+NHiR0BtDGhcwm8qWtvIDVLCUewaw+SzO0YClM1kaiAGmQzJZkcyeZAskWRLJlkKylPR8hIp0EZr2ZJ2owCsk+C0Q9whwFjZWybUlrvaEazReaE6AvA4AyIFJGwCMCHgnUsECEEYHmAvABildNRU/Lql1lX5k09+fo2Q3BVq1g4v+b/UbW78wKUimjEWA7VV5cSGM9MEFu2A7hu2j4jokIo5nvbPtkgb7ZZ

ttlFaaR86v/lzx52JoV1eLNNOurgnyrReiE9araDrBdqL1mNWvJhPrAyJ6w/SVdDMDrzDy5Kd6seX1qIHMMpRUS2OaNuGgbiMEZvX9Ws3/WgEV0aoOVuMBrCgbMOIk3Vr8r22/LYNrM+DYhorW46VZqGmtZH26W4bsN61exmAoI06w9NHG8jeambhugcUAmqoU7M45oLo9AwgzVAHj1sBE9ZmjwSnsI119RNFC6YSJzb7Rx9mtCmTXVU/hRaYtcW

hLUlpS3Qg0tGyTLeP2YV8F9NserPUEBz3EAk9vAfhfMwmqr9hFDmuas5vxX2RSdHmtahcwpZkqygAUM/r2BhjwiO2DO1HbtOp7hax1CQdWAMEbhAg2A2QGdSiznXmL+dN65FuBLS4lat1WLCrS3KcWYNeArkagStsMZZh+wmxFraxNRIQw60AlJYAdihkkCwlxqiJYjKN3vq+aaCQKEy2tCpzT2jquwTbtBgI4ZoZ/J3R6PA3VKg1UGupbWs92Ha

ZBM5HorMDB0Q6odMO51vDsR3I7dwaa57bHjlmB85JvuowXjoD0E6ulOc6KkArirh78NzgwjdlUmZ5DDhuQjgNLFID+DsAMQ6oDIeDjpAAA/KUPY0DDpDJ8d0J4KUPuNJqhAdQ0JqL0N8S9dhEhdQvmFuFZNg4phcEV01aGHhkQ3Qwk0UMSgEhxhhABocX4CLKOAh2zrNqc0vaXN6O4lSe0p2sF91PkbgRvoEgM6VGO+kdcHodZOsXWbrD1l61wA+

s/WAbINlRC00f8gJpi3nVfvy3iqwGkq+uSLqf0br4JkuxVRcQ6CmgswwS3Nlc2a2jA600iMyoywYx9JDVuu5Sv1oN2TyzVxu8fPWxNB9g/ICkb1RTJwTqjLQTXLAa2AwRklFQfDIpaun3WApj1VMx3hI1d3oAFa+rWRqZMUamskjfPA+R7rDXe7ODishSb6I9X+igVhO3tlpN6UzJcxfGQZR80HIqc1OALIFiCzBYQsHxKYqyXEBbBBRGwSkOE0o

guX7KaxaASZdQMdlDgG0zYWKe0BWVeT+lOSPyXbT3D4ggB7QIwJ8CWAqxsAFAfACshVhAh3Y+INcJFKuVNd1QoMxRL2BVCg4kpaJiZaQ1tD+QFgYMfowxgMwuj6xEKF5dSIsyJhflJU6qVilqlArJkKp8qZ7RPF6hGpoKmcRCsnHBY/MHyfsAqPuULA0JBMgaRDE+jEsyWAJHBL8khUdSTT0xzMAvPiXrbHk7xNcSsYVHrQt2mxwsNiuJ3hGydCv

NtknPOYQwVow4daHTtwBAg6VqI4Uq3Xbqd1u6vdKiP3UHrD1R649UuYLpAlQNSGyFS9sWfBrotajYuhxS/qq1I0swn0G0OdgtCKhW2vIzUIKytVE8j2zLGhjrt60jH9devIbeapG0IkmzncsllmFnM/I7eS8w0LWHW2WhzKEBSGNsZJI7t9VFumUGaP9WWiIAZx6DiZPkZwcrjiHY7rgTbGkGZJ2OuHj+iwEzAKW4fD4/wY0UlTCT6ygZSScurXV

bqh4e6o9WeoBRWmPAT6uyefoyI+w/FSCqtABQCnbJ6J1KY8jNB14WwNefsCqAJNrKfJ+k383BDJMUmqTNJukwyaZMsm2TlysrJ9DWg4JXVxoXVIhfGUYnauqoOHHh0PXGgpT00rInlKhSvLiACp1sUzOVPfKdttajU+JefnkoQV4asFWONakun6gM4j5FOd5Ow45z85gaWDDtNDgVoOYKGBudDNT7wermkoitQjO+RlpPmwngVm/XZLEz7KlM/fy

2DugHgUAVoCGEjoD0VYW4QgKuAmD0A9wKSTiNgGy0SrctGXCo4utKNC7cCDIyAfUYl1bqhoLYatNZZrCLpFQuYXkY2HQG9hXiAiBSeqCGNDmGGj6sY5EomNwHUAikZs8AYoJBR0JaBuIPWweRiswYQUSaJb34mIm1ofkXAzTNElHmjJFxs82ZOuNiCiT3JF0beaanHbMe2EWfd9wgCetlAAxJk8oGC6lr7z8kx80pJkqvn0N/8oCqZb+0k7Y5i0t

APuqiNja2kdE5CiopaJAgbjoW3fV8ZO3rXNrQIbaxFaqNRX4Wf8Ms5UZnZ1zqzsAp6fYuXaNHqtdVlUGJRa5TAz+ISfNpmhW3xAOacwDUFyLwQDnoZ964cxPOqtjnJjUDD/V+3VFMCV5y2EUIoh/V7mKl8G7bVB2MlGtzzCHCyeJOvMwaHjzu5pfowOt/ojrP8pmZ8ZZ2AK4+wh3DY4PAVR7nDBQ7xpSGID+N9AuAQkIeCAEPRiAAAHkGa6EBhfG

0jXIVcZ7h64cAeuHxuoD+DXGMRKQnxtL6cLiQ+AYgHgFICfVIiZnVjWnoVsHClbetVW+rZY5a3Agut/W3bYMJG2TbYhM27IEtuyFqAqAW21kwdsz98Azt124JA9uUgvby14TWXt9jmGSqlhgu5HHb6V7IAdCmvRIHcueXvLUAXy/5cCvBXQr4VjpjppYXEbEmytwOxrZDtnA9bydw27IWNum3zb8d4IInaHthDU7ZfdO4iEzvu2tCud2Zv4dH3Wc

VmGSkI4CLMtzTUYZRefQOBkpL6NELXL6Etw/r9rtgsZJna8wluaLjzbNy45zbesx9hVcVks/y1Bu1yH9NZ8rclcq2w3yucwT6AulzAbxgDmEhG1aD8jTA8J6NPhiPLFGwzk24SvriTY0rjmIAJulxb0gUhdAejR9gKOqOUi9ypg8OHE5+zeMAbb6Q4ChiBsONbbLRkGy9MQY8QHaRxi14UvbXfFO1vxv4t2jQt3vamG6vFmaRzImCHgEgO4FZAMW

qBjBkQVENgDAFaCcRNQ7sRuDmZYOiOXtQO4UiCAGKhh1YWKSQECEtgDFyTVIqAPoAGLMATqaOkRy/IBHQ8BbwfFSI0h8gM3eDvy8W6OpcI6yDA+s3AESfmkmz2cZsu/FbMtkpIbZb8L0I7Phxq5fZbsj2X5Ax3OOXRvsz+LZiTtz86yO9i6xIEJWWW59PsfMMfZWlyLepvxCgrePJ4rIXLEW1Mu0BSQXA9wcAS2JfMPAvAEgKSfAAMCMAJBCAa4Y

J+frv1mK8tE2WKzlvukJW7FwvBo6lbJAY5qB52NVUog1VENFo9bZUJtnryFh/IXisqw/jQcDboSmDsm3/CtUTa5430dUA6st2/DV0zq/dfxXfbUOMDR2Y0VaBGh299zzN5h4QdYchqSDfN8g7PXQA+lCAfpAMkGRDJhkIyUZGMto6ccNk9HF8PcBkA4CJbYIqDx7f9rFyA7xHJ2g0kaRNJmkLSVpG0naQdIhbhHyddJ2wbfn6Ccd3B9pe8ZOtE7z

rs0rHitcmHFZ5QOM6M1U8xxDg9syi8nluEadjrMXHAbF4cFxf/WwbfOmKwLov3FapVj+2szDaWfrVxtc8EpcODzCYDeRU0MaEaDNB0CBKxz8mkTZNV35X1b62UdIu/ZrNqbNDjbJ4oJl43Gbm2g8xBqBd3GgV817eT7ueN+7v5aGsW++fpWCGpbOG+wbLcj0uIu9MeijabEwDGbggsVczaV38FyENY/cGoVEJFBqHc7qCzu2m/NQZus3NIBBcxvz

eFvpAxb0rmMDLemGRNRdiTqXvMLl6O+0mhYXYYkCrgWnbTjp1056d9OBnQzkZx3scOVuM9Pemt7xtkI5uG3HAAt5OhbeluV71myjmPtQ0iLfh29rZvS9rKgjHid15o/FJLSJnRnyR5nX46zXRqyXcayl4muTW0ulXtclV1M7VfjPqjENxK89J1ci7OKYrniuvBBzntrd2NQ0EWCa5KKr8pJE9oQ262DmTnUB9BzAZqvOuNstpjeGtFzCUJT2MlRc

wryVAQxzdsRq5rDnLNFKqsODY9kNad4SWrz0G0NRw/dFlqFZ5BIWxgI6XRuMNsbz87hf+MEXmnrT9p507eDdPen/TwZ8M9XD3uakqY7VJjYSWtgmtGCTHMxdajOrsw9YTKT5C+QPAcLvx7yeJ8WT1U+igU5qq1VCmdUIp1Fpc59F3yTRyZaoAcP2bGXzZmuzxfK48hGhZS5gTy2UwJflNFSlTtmTU2qbbFSX+x7mHUzKD1PyWDTSlo01CrXGKI8H

k0aYGaAWABRfTYAAsHWCEaMWGwi3EaCZdCPT7HHB9n2NMGQon2KoloFrtmD7UIi8XzzD6/fe9K+kmIsL4MqGXDKRloyN9os+q7KOTPga0zyK7M/AEyr/74uwB7q4uYs06t6zikryOufcWoYSkYRD55v1XsCbwxiq6MdHMXParm2ZUKunjPok+wRJR54imV11a15ZM8lpb31WTQnTfzpm/zfwMnGWHQbm82C548fz+PsHgtlG5R6+PUj3x1JGJ/zE

AnJPY7mT3J6neKfZ3Ln1ANer4GCm4g/kdC+vF+d9gPHbGcz1Bks/I+JPBSWz01WCltUOq4U37VciuXLn3P0xoJN599PRUkLpXfz5aDXRGhQcYOf4bo6Mz8WCpQlqL0CrEuJfBxCXgFUl5BG6m5LrOV04pfBXKWWUJpm77K3u8VcxazpV74KPiUfe68NXgpzy4Zegj4lV7rk8aPTA+u7mV9/kNK4dZnbMy2ZXMvmULLFlSy5ZSst+8v0zfo0/7u6V

WeF2Q2lvSVlb/WaAc40MEn+x5N9BPaahVQmE3S8OEHkO6G0u547z1sw967ibOH0m7VYLT4yCv4psU2DApbkfq8s3OtFMFIT+Q6uNNxaFmkUT7GWPxxwNbtqIMgv2HaHL3QD4Q1PG+Pikv9MhWOtCfTrqI0TxZ6JObKL4IIeYIQBBDtADgyj5wKeCzqWw/IQIVUnuBAGLKyQWNGySxcyXTQqGXaySipAtCU+eMeFjZSj7p+NUgpLVEKe1TCldVILf

NPSwoIPPdq3bM9PQ5SwlVQGYAbRNsXBnxNpTKX0EthLYqRi9pLX5SV9VTQFVt81fbzDS9wVDL3YMFLCCB6RbTNOTFNNoVVgv9eURvzKVHkW0H2pU/K31PdCner1BEfIPHzjlbLKvERwa0YhDqc3fSpmHVH3eHxO0Qdag0h1odWHQYMkdFHRD8JnaKz/djvUBkpFqReK0W8ytOPzrNtgVuTf1ZgShA5RurW0B7kz1TCRUg6wY7C89FxWYCOd8bCA0

JtzvEc0N1cPCgWG4EBeY0mg14L6EBRXXX4SVBiEDARGgkKJRBmgeJdUCFRt8cpT9cAXANwH9gXfbRH8yDcH0Fsp/ATw5c5/PfRsxtJJf2/NiTaz1r1otWLXi1EtZLVS0VYdLXb0cfPH0v9ukDMGmMBwBtD8hkbeHGBRxfNFz+VVlLIJf8fzXIIkAD9fQCP0T9M/WhN2fZrhCR0JBgRrQ05MAK5BgZK0A1A98RjDIQLuCXxlNGxSL3eU5fFAIV80A

/5QwC2PbAM4cVLPAO19MvTXwghxgGljcDOBWj1mBHkHS18DxgWYACCVIIILoxGAvFXpdinCuw4DW1ZXgd8dPRgUGN4jCKAuAPfDmV+BJAQ4AhBNAQgAoBVwGAHWQdwBIAGAVYJ4E0A6YFZCohY5bnSm9AbIkFAkI/JdUgkgPeZ2bktA1/TF4LmWrSUhrLWB1T9kKTNG3Y4lbUAbBQcJtBFEkHU73KtAwSq0u9BuPD1QBrnG1VudptNA2kR5tV1Xe

cRRIpTtBpgSYDlZe/F3X79a1d3WDcwXZMmYC87NXGFI/IT4HxAVkPEA9AI2Yl00U5yBciXIVyNcg3ItyHcj3IDyFF0ZczyVaw4AtwIQFggaIQFBSR2gAYlXBsAFWBSRYIKjWRB8QZwHtDdrFlzcdlZSN0D1AxLl1q96XatlKdpFGyxgo5FNdDxla8Trw7ZMkW+32lUzeqgmBdQ/UIOgxnSP1FV8QxQJxCFvWxShsFnFKzA9lnE7ChhrLUyjrwfIT

swRsOvRdA6BoRRB211OQ4vztdoDQbSu9+QwFABxuGZ72XkPXVAEK9/IKAghx/nMfxZs3dQfziC/eUfzwNx/ctXDduDf3SyJRbWHxjdURLDVsEQFJNzEN5bCwgMBuEPBRI0e9FWHdA1bKAEY0G4aoWqgMkXw1T0WFPQH0Abw7vQo0Hw0gCfCXwtgDfDcQD8I7dS7YvWLspOUuyk1qqavUU5GVCEKhCYQuEIRCkQlELRDfgDENjkHDfTivDfwh6FvD

M9QCOAizNV8NwAQhcCOqBPwmZj3d17OzXH0t7f4Wt8lrT4IWl45Q0Hb9SnZOV8hauaXkTNUwHMPSCOZNfw38t/QQBgBd/ff0P9j/GkWxCAPXELFU5vAGyrDStNdWW9NAtihj8pddbwzBNvA7w2c/9HsA+gjPG5jrxWQjXg5DbAs725CLvRwPL9+QwUN4C7Ve5xm1RFZ53FC3nd1SlDj4LUG+hvoW4MYd/XAgxiCQfXmy49QVB3GtwEw1ayEAYAIw

FXA4UL5gdD1Qk7RbI2yDsi7IeyPsgHIhyEcjHIHHBlyNDZBLYC98LtX32u0A/O7WD9iomWXrIXHDg23DyCXHXZd8dHxyPDy2blyWs4o/lx+DcrYVzssVEBD17BEzIqIfc77J9xO0EopKJSiYnEsMJD0uIG1VcKwpSPUitXLSNA9dIpo1uVopNsxmhD1E1y2dkDHfC7V7QG0AChrIvsNsiuQxhntdaaJyOcC0wDMApIvHAAjs4ofNgVGALQFSBgCF

Qo2WiDlQ1cPuMooypTDdWo3cKjC+DYT2PCKOYBRENHGYaGcYJDMIUz17YKuFgBBOA4jY1UYqQnRjK4QIixjc7YhSgiu3Jvh7cHCcu0qYq7JCPQBxIzf239pIvf0bgD/CYCP84AE/zncCItKkXcKNDGKJiYAbGPFAGIqziYjD3CfUHhWIpgJt9z3CMz+IHffinxJHLIEJaJH5SaNzDXLCQEyj2yT6hyjeyfskHJhyUclkDpveQNm8CQj+yj85nGsN

JCdI96XW9awQyKa9tvE6OmATQIZDb8XiAhwON0PfsNtd7A0v2HC+Q56I2wWwXZ0hgugKOKPYIccj17B4gEUAbR6LHJR856PNHFVYfOdCwBjAfJUPY82HK7niC7zcMP2tkg96Oh9ow9SVEjPlH4yp9l/N/wZjJInfxZi2YjmK5iKgqYImU8aDHFoDSHUaOOx9MJ/z+MafboNTh6fT/wc8f/Jz1Z81PMUJZCcvNbjX1CwDuIxNeKPajow1oQsDRpjQ

ML1WDmxdYLbF5fZX0V8dgrUywCUvdXyO1DgrXzHEdfQgOhVFWCOOxlo40HFXFeUeOO1Ak4+thTjN4N4O34lrOWMTC2getivc4TGXmpDEzd/kECpo4QJND5yRcmXJVydck3JtyXchWR9yGukm91oiuXLCIGW/VLDl1G2Nj8QPTdXrDV4Fo1rx8wGsFFMVtTs2HAmQoRGck3JG10qZ7oocPOcQ4mJTlEmzOjG9UMLMJCzBljYhGoFkDPyAIcAtTc1B

gGg8mVhxs4qpSB9A3CSVBjC47jz2sK1SHxn8Dw2tTh8BDRf1rjsglfy2BwQyEOhDYQ+EMRDkQ1EPRDMQ//1x8OUcLFFQ4RXzzkwOvDgRFYfnPDlSUQUF0WzEOgqz3gxHgMePs9v/Znz/8cfWeNoC/kLwOC9efA5WQtMweJXFMsBTo0uieLZYIQC1gxUw2CvlLYPVMT4tUzPiGpC+JCx0vY4IIDVLOVlowQcLxTlZ+E1+I+QhEv4hwkxErz1/iZpf

+MkVAE+SCNBFY9x0kpHdVWO2BX7O4DC1PrTRWdDXQ90NaBPQ70N9D/QwMODDTY5SJwTlo7ngpErHbsA2i/7DQO2iHYi0Al55jDeQGt+TE6Jl5TQJpCGQ8lRUHLMbI0mjsD7IhwPGMnozhLXY6wEhgoRKvShBbMSHDMHTBvY3yCAMaBdgO+juI+3U4Z5QkKKiCwo4GNiClE9cISDVE543UTBPQ8NhiQxWzC/NOgnIP8TkI4xLQizEzCMsScI6xJx9

8wU7B+QQdS5OVQqxPn3GVSGMhDrRQDNyX3UoYQeOp9fJEeIgAjAbMCEAngb0Ie1VPSsTiVHTPkUUgC/fH358MTBtARM6bBtGHBifHeLlM94zJIPjNgo+O2CqpVAKBVUvDXyviWpUpOZdTg+oGoC3kqVIckvkvzHTBmubsLlZREhSHTAzPScQlQeo2KObVoKcoka4r3d5L4o6LRMy4ARI0ZOFIuU+YB5S+UxZM/tVo3BNWT6edZMA9o/YD2hsSEna

Lhs1ePGmOxvoQRnIRjseXn4lVjX5K5Ex0ZhPhk2Ex6JHDQ4mcIbQHiHBApl8JbwMRQlWDv2b8X4uYAYdfXTViYcgYvOKH8C4uFIOD0XcuBdC3QmAA9CvQn0L9CAwoQCDCQw+qPTUmXLHWLi1E8GAwQbVZFK0Suo6xlD0qORGKcFkYlwQkBNhXNzgA8QIME0BuCOITLBAgPoWL5zNDgAAByKAH8EEtUgHxAw5IgEJBThaIUiRtAVABBAb0/QEFgqR

EIREAohLFBkh/BdZGMMP07SCqEPBZQEpRlAQoXaFz0hAG0BNDVwXcFoMqoUPS7AXABPSYAM9LSFL0yImvS70uIXdBn06oCTtCAN9NaF1AT9O/Tf0/9JOFmAIDLPTYhcDL/TaMqDNzdYMsOU4BUAJDJQyRhTtzE4LDWCN7dZhIRyqZB3auyBV8IpwzQyPBDwSwzj009NVML0u4SvSDgW9JOFH08jPgzX04DLOE6Mn9L/TsXJjJYyQMk4XYzIM8k24

y4MhDP4y0hQTNYpRY++yCNRFE93eCNQjiIa8lURfUqctUQ/keCRTRMzYBQQk7TGBJAXojgAIQziCEA2AN4H0BnAIQDNAKAIEAuAUkKdMwT8EyNI54QbVSLBtf7JNLqN4/MkIbNz/H5JxsrAuHHXkujCqBM8ZEe1MpV+KAmkLTTnKqzL9S055JuspWBYHTS2vXdm4t1RIcExtE48hAod6WHiUURwHHCQXD/vTcOXCgVFUMtZzua1mUToo/F0ustQi

+BVgeAMpAsdMAPcDSiuHC+FIB8AfEAoBWgE9JBAdwJ4Ci1VSN4AuAXgEEHxAxgDBJ1xjxHRzRdjQ4UgoAOANZCJAHgLcHxB5gZwHoAjARuGUAdwBUkkgooadNYMmorcN49v0JYDw5wHFdKD0G1Z1JjlfMm6xd9+o5oEhFwYV+npsJXN30kyoEzWKacIAXbP2z8QQ7LDTsE0szrBv7e/U1ctk4hMWdSE+SD8gHiT9mRNFRFtIBk0wLoBecrQEUGRJ

JgXsNvV/YlhJ5DHIrrItU/4QVDrBTeWtKnDPnU/ndVIYWc1kTFs4H0UTVQsGMeMWolHJzYASEWxh9V01FPXTTwrdLlsU3Rjn0AvWeYGjsTOefnSBUAAAGpUAXwQgB4tQSFSYKM9IBfBogXIQgBy3XGIqoXct3PiYq+KIR9y/cgPNIAg8+DJDzmAMPL9ySY4TnEz6+ETJgiW+OCOpibDGpnyRIs6LNiz4sxLOSzUs9LMyzuY+TOjzlAV3LY54873N

9z/cigEDyw5dPMzyI84fWX5bNGzm+EWIsM2KI9mTiIFdsSc8SGi4qaYw8cutV3wRFTwcLM0VcABIBVhEIBiF8Z1kfAAoAKACUjeAjAdoDgBoQdCkWirYssOZzrkwrUrDrYtQM0jtkxNIdjRkbMDMDirLoGPYj1bNPXhlQDr3NA/kFjC10Zc26IHDA4h6NIFFcicw4Zesr9l1R1oFUUURhsuIG+gxs4hAmypgHiXxI/kY7GQpFwhbMBdwow3JWyyg

JYNaCQ3eSxiicc2umFIuJZQHaAXgU8DlBSoig3QAEgA8C3B/mIQAdIIQbAF+BMARuAGI9wZEE4hfmZMQ+yw2GdMdCHWGoFXBFQSQHwAGwVoDkdJlQ4Bz52gXEAWjNs9HTDCYeU3KVkwcFUAI5NEzHNzxsc97j5dvg8okpUHfRsCzQFQRxKXyO2MTVWARkvrwvg6ChgqYLGcq/OBsWcgrJ/t2c4rO1dn8uAXXElQXVRwRZQ4REcK4PU3QQF6WDAUj

iRoMaJsDbkuyNYTsPYOJlEy0jeCOVa8dXN/YO/KGEuxMBP70iClwwguhSIozj3WzwYif0/JDCgRNSCUU+fyioTwhGJlsI9C8Mdy1CZ3OUAeAWPLz4jEdvI7znANYGlhUAXvPcYs81DKbzBi1vJGKfcsYomLQI6YvDzs82vmEyrCUTMLzc8+CJcJEI/JHXzN8zQG3z8AXfP3zD84/NPzz89qFWF53Pgn6KFiufjbzlipPNWKpijkD7zd3N4X3cN7e

zVHzzCpzjc0iVCMwdkHfckia1goy+wRFBgnrxSMBDYUmORK+IEDOKjALcF+Bq6O8Etg5iQ8AhA9QnwuO88s/wstiZne/OrCiEhNK5yk0oaGcA2jbVSlycTChB3Ns0tmmVAjQRrkUR5WYAudAMPAOPuSg49hJyLus4aBl0MwzgSrRMZWOLs5XFLY0tB4zOE1ESeJRgWl5eKPXKqLO0maytY5rNUMWsXUvlw5l8+N4B3BOgCEFIA1FFgohdcuc7Muz

rs27PuzzcJ7Jey3s0MKJcyoiQH9pA6YOlDpw6SOmjpY6eOkTp4cr7MRyIYxosvxmijqLfNUUsfM1CL3d1zdSCebyHa1ZoMnIREh1NwumiH7XABNKzSi0qJLcs8fHyyyS+bwpKNI0XS2jQit/XpLvoYGWyVfIEJFRzwU4SlGAKHP/PRoKCZjAoQ2srDzOcS0jhKVzv8PsGVB/kQot4AJE1gn6QQkUkg1KO07mw49QXY3LH9wygwsjLjCq3NMLY3Do

ultE3bop3TxDUiE4g2yQ8GZNG4AYCGLSAROz9zgAb8D9zE7fovmBI8n2y2AdwY8tk8zyi8rY5ryiAFvL7yqYpdzNi/O1zzoI7txLt9i4vIHdbDGTP4JNAVEvRLMS7EvxBcSi4HxLCS9uwn4+CN8pPLPyy8p/K/ymgAArm834rXsxY4fPZBJYzfjjDvM0EpKckyn2HXir3GXlbBcEMnjd93s960RKNFC8gCEEAAYiEAHgU8D3BLYYKy3J1HZEGYB2

geEqFUSjckt8Ko0EsrWics8GzjSSQ5/TKzE/GjBGzokvMBmB6wVXh8VRgEhiV5GkUHBaQWywv35K5chyMeSoC7B1nlxSlYwCgpS2vF9VJw/LELR3knVVXQ3iFsF6s5wqbU2dW0oSUqL5y242IKnRL8F1Lly8FxqQDSiYQ5lYIRuHxBVwHCM+AqyK0tWtM6bOlzp86QumLpSAUunLpK6aujdLPuD0vQBZC+QsULGkFQrGA1CziA0LSALQokKntUMv

YMkciH1LiNEzcpjDIqOMr6irC+fQ2MQE1bRFQnvWEo7Z6pVwt69sy7h2SrUqj7X5SZKsuUvziS4stJKlKpaKKz402sNW9uc+tl7kr1WvCJ5McCln3ZurW5DJ8FEFcQ6BeykvwgKkZLBxN0f9UcqrRBEy3n0sr1ASWCrqZVj0HEVQ0HxirEgh826qMcvqvvsdyhN3x8k+JGIhwi8I8pPKQQZEL3A8KjvIIqHyr1h4BnylhWwrZPZGpVhUa78vRq7y

wiueKgKsw3zywKsTKpiK9GmKOL5aXiv4rBK4StEqdwcSskrpK7TUwrGOPGquoUatGpvLSazGoGKSKkfTIrN7YI2livM2WI6T6K8/yzTZ85Zyl5ETfpMmqBIQswRKhApEtOzbSq7PwAbsu7MIAHs50teyOKt+1kqyy+SsOUb82NDvy+eYkNtj1K+2LgFjsMr2bBICL9nmNs0jmma5kcbtS3FMpe6sHCsi4Uookhyo7FIYugfyDsLmMQDgXM7OUwK5

gylRUB+kxwr708cbeMVPt4KiggrCr6ZQ3KBq6ik3ORyfRJ8zLjZ/Voqrj2xGuOf8/EgTDkE4KgYDRKHgDEqxL6AHErxKCShpxx9dLVVkANkPJRBWNl40hlmBfiVAv8h/kgtAdTeLNoIxT66wsQvhy8oEBizDgOLISykslLIeA0sjLKyyBUq5TiAM/Yli1FEcChEqCaUlKVPx1dR4h/1vY503gDnlCLyVSRLFHkPjdg4+I1SckgpMgBtUy+N19r4u

lFviZxPBmoF3HWOtXR4650iTrng3MFTqAUIcFaSwjFgIjN8wI7wJzkysrGxk19BMwGTcARnQ1jq64Ui9Kg6EOjDoI6KOhjo9wOOh4AE6QspWSSS22rwTtqoIt2q7Y7QIpDnAe4knqbQZcXtSIYOrInLecn9ERxjsfBnX0/Y0AoFLMi/ssgLBy6Ar/hVoYRMTjniFyUm4ZQOOK4adPW0CzB14tsF6scTdqzVrigfAuGt5Eogp5taintJUT50xFNLi

XzEwohrsy3RLrrh47FN9gm6lurbqkKlCrQqe6oYOFB5MS6KkpyEDCw7j7JOvya0fiW5W/UWU7xM8kkfdlLcaRSIi0kBKTak0WBaTek0ZNmTVk2DL/GgAP7ABWeY2bYKk8+tiShTeIBFZlIQFC7VdsOANnqVgxVLeVlU0S1VT369VNi9MAgBMKScAnVP/q9Um+JODdU+oEUaWMaaBUacrSoLfjNGhRALBdG9jEdSksOMu6b0Gspw2gr3P6PlYbmOn

U0ARQVfOFJsqnOjzoC6IuhLoy6Cuirpza4o1Wq5K9auvzWcjVxqNgiqsppKHYtdGVA6MSaGxtilARphFpEb6EK9iEMWijLLK2XKLTQ6gcpFKI67iPQF2zHBDSk1oX2OKByPBE3NcAUZ3x1BrA6cPFpGMARD8qIU0KqhStS2FOklrGvQtLqXjcuvsbeqyuNGTnGoeMSaG63CiZqBKoSpEq9wMSvaB3YCSqkqbEqgVyVbeKANIcozJxOmCoPJSF7A7

nKgnqaJfHxL0TMUgxMItyTVJpIsMmsi2ybKLPJv3r+EMwPIYtPHkzmAJaUVoF9bQCBq1FDPSvwCgFUp+uaaX62tTfqtTeLzySumuWp/qikrL38x8Ag1OGa1xEJFhb/krkQBaQsk01Ra3VNdAQp4cLxUQa6vXLloqvg663LTNiFrxMoFWMtDiN1aiQF2a4cghoDTV/TAEPBiAEEHacHqC4GIAdwcEOIBYIIwHWQVkVcFe5sspaN/dpgxhqjSraghI

fzKyp/Nea25RUGETIAjaGER2ArWG1BWaMJCCUrmaAjSLWWMAsFLHq2A35DRG0/E616bORGzqG/e4kCVKEQmXjrIZIpWNEjfTUDnKiWhcrcoSCqKtnqKCvpuND4q7bK2BPgF4CeBu6KLKhZMqh1gmBSALcH0BPgNgCeAQQNgAGJTwLcANpMAIQGMgftAvTirJChHI6rVygxgz8fK8Gtpb0eYEq2zQRJhKVqGufyApk8WnZpmB9mi+HvbH2rcGfa6G

ptoF8W2yswdrVKp2oAcE/NbyzQnY9SECjglZv3l5yUtq2myVjEVODrwC4tNkaoW+Rvy0PoP/A+qG0tmheJAcDbTbTQosxuqLC6yKOLqVyhotw5c2JFv3CaWjWRtyQ9O3K6LRDA8svCJACjUUIyNC4F8AgBYWNy4o8yqvNRjO0jVM6ukSQAs7SYkCvJjxNSmJk5IKhCOky6YiADdQC2otp8A4AUtvLbJASturba2+tsxYHinmOs7nwhQhM6zOxzrF

rB8yagBLmIqWoGrXU1ZsFcKnTgJchWQjoFrRcOk1H9T3CrYEwA+wRuE6AjANgGWqLam5rbaiy+5oCK2cp5tYbna9hr0iU0swIKLLQFpCHaE5RpHiBD1ElRaReSk70kbrKh5Iwc5G+yoRZjQaVga1OBPLwnD1GuzjaNerLxTKVnfcouk7IU2TuJajcxTs3DYOiN0Q7NOtottzOivcr074avghBBUASkW0ybM/wVozMMvEDEAXwV7qWZT0g4Fe7IiM

OTkMfBfwXjBOFB9IXs3bYgC/SQQKABvTwhDgD5AXwDJETtNAeuG/T/BJ7pIz+GfjMnhXupDLh7gejgD9zQe7Pj9z/BdWAAgThNgAuByejgBgBOM+DJ4zqgfwT4yBM/wTmL6Yx7s4ASMzjPxAP097qMgOQVLv0g8MjwWL5AevQyoiSeggEyEXbSHuh7YezDNCBWAaoBR60eh7sx6mMrsBx6KAHIUCACeqiOJ607P3J8F9ASnsKELgHwTp6Ge1ACZ7

4M1nqcz2eoTLJiqaimPAqI4awygrS8vYKi6O7e7q57nu3nv57UALDM+6qhduF+7w+gHooygeqXrTtZexeyh7v0xXpD7le5HpqF1egPqx7teyQEng9ehAAN6O86XvwATeinougqey3usB6e9wQoy7ehzLZ6/UlzL+KJqQIxHyMulDqKc42yfNbVa8fzLy73oeE2VR/pGrCvtdm+rFK65qjF2hAQQVoBBAOAB4GIAOnAtEOB9APcEPBoQfQAHAkRC/

Nuamuvwoo77a9tspL1AznLrDaS4UBtAPTKOPxp6WY0B9qRQZrjbAGWO5HG6i/KRvlzbK2bpeq1oT6HQlklLKV+jHVeUWEQfOXJW/VLef5MOdU5I9oO6T207kg7Vs6KuO70o3qKy6OZOAF+BsATiB4AdwC0GOzXtTRT+yAcoECByQcsHIhyocmHLgBs21quBFUXaQo5l2CiEE4LmMngr4KBCoQpEKxCsqsx0QapDTAbPHHqoriLu2MLYib21gIp0M

OhXkwE+43Dukd8OrYAwGsBnAbwGd+xrvoaNqg/qwSqOwhJP7qSs/odiuKNBEgDB5ZsoPofa+OPdiVVb6E1A3iHjtna+Op6sudv8ChHRlxy+tOxbWzCklp0CWvOuPbwqixqXLjuvga4MY61czt5K663Mu7tO67phq8NOGpRj7IEQleKRizxn8E/ciOziI+NLQmYBtATIekJ/BWQkdts+DO0h6/cjnuwhkh93LbzvGDIZTtZCHIbyH6h4IGKGCAUoa

ztyh53pc7Xetzvd6POumpLzFhLYD3Bp+2fvn7F+y2GX7V+9fs36vQhvJYVi+CvhqGO8/IeyHIiXIdWGihtO3aH3bToab7SKlfjS6JYoEuoqbfHzLQ7fIK9x85DqsU1w67irWugSdarYBeA4iTFy3BSAMYB3BCwEEBHpTYd2ASABCBSPftd+jQea7SytSPLLNortoMHnFOeUqxQkQ6u9jzq0YA/1yZGEUTjB5ewekaOs7IvDrBOwV0EQ/+iGAAGof

BvxmBqBCBuVEtPQKKBS924kYJo1OnOr27CW2AYCHHRBAdIK1sqxo2zaB1DtYKIAIZwSBfgRwD3ApZXQtcd+BmOuQ8Ny4QZLY2izLssKE29OqkGCvKAh6M2KwLl2b7HHNrK6egwgCFGRR9WMAkGuiEetrm2h5tjTdBx/NP79q8/vg868eIAnriEdMETiBuiqE3YleTrUa42jArRAL0iu6I/6ZugTrm7+WS1LejxyxMtRw5IE9n2obgmAdzi4BtcNJ

bQ3ZToMZXicBJaKoh6uqhqw9XToSHd0qfhL407JYdSH0hx1maGEARoYAAqPYewIrOyoaLG57Esc9zah8seHtggasdrH5bSmp2KC8uvgOKq9bzvyQXh68AQB3hz4e+HfhztgBH3beYaL5IiVoZz4UhlsZWGKxzsYgAB8mzWF7yKo90c1pav+M+zpqoaqOYIGpisbAawM0CxanCrYF2aWqziu1ruKi+CIHNAQHOBzQc8HMhzoczoFhzSO8oxtrKjZQ

PihNk55uhHbRwwblC/aqtPPU14ZSB9qzTXBgPoeG+Vhba3+qbqFLIWvEZDGo0etkLQuJOcNo960dUReJGs9bkaRCaXY0t56iFVTW54xn3oLrAh4f25H6i/QspalJIQZhjohjINrqGW/Cw5SRhmfrn6F+pfomAV+tfo36t+mxJpZ7dOUKaRdxCidRN+fUet7AfvLY3ccgOFoNuA5WlxsZbF6rYGXrV69euryt6nevrze63pDPsZJ7UCwQwmsSnNBx

KdSCCU6ia1ul8kA6L2yS1U3JM/qPJ7+uBVemv+rviGUL1rnTDUtcRwnWjKbUYlFuY5J5RiJxiUC9yJroGjaz3V1uPGcaBvBVHbQOwpFBGR560DAxgIo0pzCGi+CYGWB7gtwBeC/gsELhC0QqMBxClaso67m/fotHVA4/utH9BsCecUcwIhHy8BrVSaNbhc+rOImrBn9FyVs68A39GZ27Ed5Dgxk3WNA2rXyHJIcbAr3VEf8U0GhhgkXegedpw6Sl

+8jGkDnmzTGhMbZH84zRmBqEUyf1eNqW2UbrVOJhH3nrXGplrnpRhwSYmGphsSdmHt+/JvD8OkRSea5sEHPx8gzsOiQ0n8UdoPlaF644o3yt8w4B3y98g/LeAj8k/LPy+W0hmpZngvky+ITPEeszALIwrsqwrmDoBlbWgxpptaZffeNab3J9ps8nOmlXyPHf64pKODBmspJNMHR92U4FnfavCvH6gCrCJZjXR5FJ4clBZuZmeUHpFrwxoBaekoSP

ShGdJVpiJo2npleYCSmaKiy3jauI3gCWBkwwnMvF92/ehkUBk3Zqy0J+mBO4cUmtJtIssmii1ybfxsP19GmGtaqJDqOqkr2q6O7nLBlZuei2TxvPUqxOi+TUBoAK1tFsBtAgUm5Onb3+myqDHMJnB0tBmzcZrBh0rXGUo8lEVkKXSvNQawbSpKPiViKmRkKr8GTjUa3OMYOCawvMubY6fgHhHMgsYnkxygv5GeHR2k/FnaH8Vdp/xHgd0cfsi+HS

NXWd1nWscjX1n9ZA2YNhbnvsiqoQ026E/UzMe6PugHoh6EejHpB5hgZO19AVcEOABgcUkOA2iYqPXp3S/keIafSshv9LKG6htoaQy+gZQGDmrOiOa8q05sKrzmkqvNqNQhqLEdh599s/bv239v/bAO4DtA7WTPDuPnGXMMtTGmwtHMZHIhrcrPpTh1AcVG1Z99lJUAsqvFBl1pvaZQpR+m8gUGKqJeZXmBiNeetnzYzni2r7ZlSvnYnZthvJC9I0

Xw+b60ArAIYfqgaZ5zldfGgoYsLHsKxHAxzrK/7x8VsE3Ey48jy+jjKNPxrBCuvAoOn/qiQEftxrY1nMkhkwGoU6mJkuq6rzc3MHYnOorTvsEN09A0ltzw/Tt6KtgNjgqGdFroYKZXO/lwk0i8gYa96hhpVuIt0mzJvIscmqi3uK/exjj0X9h8WsOHxY9Tt3HJ9cBcPHcc+RVbAHfF6jbN0yo1F2a6u4ZNmrjZi+Gfmv2n9r/aAOoDvwAQOsDp/m

G2/BbI7FKyNIamHZq0c7abRl2btGNRE0FnRTKc8frAl4rZ1IDR292MinJ2iRommw56btYWZp2eX5pcaHhoZZpePRvcr5IHmbdU8vKj03hKJi8ZZDh+7Ob+q+/Oif3l5OyxqrnZFpIMunzuuUerr6WtlN4mkmvzsLbi2oLrLaK2qtpra62vlov8L6w5SgD4cRpBSVDPcBtZS642n1ghTZ1VusWNWq2Zx9CltP34koA/mbKXjWleOqbAUSGCvwfkVU

DGQH68LxcnZfFVMpnHWpmXQDT4lZt8ne0gKc9b9U4KZ9beUB4Oa5kSWcyMsnJOpP0rWaIeoQKejADiAaTTRstu8L8N+mqTaPHSx6XAcOizW0lEJWdlrkveWunyIcZNoeD2LMeqCWbxsYCS4dRyfq2AqqxYAUKlCuqoaqmqu8fq7Ml0EaamWux5sdqiFjrpIWmjfiM+gf8PuUoRdPLZxWMAcGsBTwX4vcWYXw5xpcjmpjeyViljXBJUSUqELpZhxK

EvLzPF4WzPwbTMpwcFQbaJgGpBijumRaU6WJpFMzHQFtFMyDwZh6d0mRFllpZr2Wzlu5bOavlriBYArdvrYfifBxsnzKOYyf7jlQcBwQrl/RLf8Ti6GdhmrihGZuLkZ3usKXN4+cz5Mk1mJMFNR6rC3hbQg7G0M9nJxALBWKZ9FBpmP6ztfDNz4vyYZmAG+oDalvW/puhUdnH4jzYVIdUGtX/8IoDtXtRTGReInVmVsmknUrxcjxzhlBp4j6KonM

sjG0DeNw6QQVBfQAtwIwBBBSAcYReAMMT7WhBLYYjs6AtwBAHaB4s7BZWj/xuVctGO2krO0jOupowmgUClURNFzKtjrQl0ZMHGUQhEW2Ym66ltCbnanA0UsXbKEXyBdGRELOYb88wCkbPU7vTDa3WoxsrHhxXJIbN8HDpiZbrkaioIZ9XYq+MLQGvraECZMEtVcETpX2iRykcZHOR2UAFHJRxUc1HLls0dFgQef/m/V5Ax+IBwBZZunRBmWIgWrr

NWbjGpBoIL5N45/WY9Qj1ta1o2gQeja1b6pw/r36FKzaoyWtNghc/WQi7trf0cW0Bs0R1IZpDdGxSy1LHC7nZtjQkjVhpdxHhtLCflARyxDbXbE62kcCQNQdmkGQpOnOeI3PVmFO9WZl31YpbMEDiRVFRN7RMw14Y3criGNFu7scWY7cewcFZCPIRoj4MuQj5BbhUCNcZXDX2RxrYmVLbjt0t4IEy3AiCjJy2ZIbIVfCCtpoSK3II7od7HqavYtp

r+3LzugqfOk9bPWL1q9ZgAb1u9YfWn1sLIwrO9FLeUBY7C23K2ZDd8Oq3cturfy2xCQraMRkurcYPd3FyirEUO+5Bs6SKkz1LbBBB1C1w7OIZTckdpHWR3kdFHZR1Ud1HXjZfW8QhdXBHCslhrUraOjSvo7lIQVg3QFjT9l+a5UnijBwUi5WMc30J/jtNWjeH5EzAHZL5rw5AZmUtm1/kv/L4TIKCmUnLced9gKK5s3OqC2VwkLaLqKNkIdsbDA1

P3YCQFxxpgTll65Y5TRFwufEWprXurQRlxc/Ezr7dYDiqC7JTcX+IKGBJKw6lgHNYVa3/XrfPWoAS9ecBr129ckB71x9efXe6mlkKa68OYAVZN4oV2NayzGYACgeGoL2vEZ6tJMfrQV8mdfq2myFZR5oV/JNhX6Zj1sNNhZs4Oh2Ag7qWV3qQkFqNTrQUBqXTI4ibJUhiVnlCESbmAh0hgq0raBnWSvZHePYaktHbInGV9iK76fFmTd4jLxY7HXg

6MGEuvHM2sYCohlNziC3B8Aarp3AIQBIHoB5gDgFaAgQIOk+B6AN4EbhNAK5sUjlKtJd02Vk6VZ2r3t0rJdqTNpyVOwFgAa2mBF1wypowQNlxVxJMNiysjTUJ8FpkanB2qxwRq0JOPJkYLNyrW7ZtdDZH35zO7yQKO/cpy+gTlj1fx2yNyucaV/JqgosKEqk7SohTwf1k+Angd2G/omNk7Qu3WN67c427tnja0df5u/c0UDHIx3dZJAUx3MdLHGQ

Bsc7HfjZg6AFuxpi2uohUak2p89/RgX++xaAv59LC+zT30AXZrqmZqritjdhSc/cv3r97+jUHTRxqZ02tB5Spb2aOtvZ/W4bVUeG62wQFEbBFQQmeA3+aWzaysVeJHDB3YNp5OhaZwkbPRpxynhePh6bfKzfpd9pbK9XCdsLZO6wD+ZYDXKdgQxzHN0vMe3TktlxmiIKx/IcXGdh7OxQV6x6e3ttV3LJk0OIerOy0JmtgxZ6GjF9zr7cvg2mPyRs

93PaMB89wveL3S98vcr3q9q5rkyWFPQ8jsDDgYSMO5ekw8iJNx/4rcXofDxaljlmlKYTbUaB3zSk4TZSRH7NRsYCOyjZp4YkAv9xcBMczHCx0EBAD2x21HjR6VbI7IN5vbe3yD79eVWqD1VWgt62IjywsbB7NN0rpWbcQf8LsaXL5KwW9rOmnId5XLoTVarxTuR6/DJW6lHRndg9kggm1exa8wC0DOWal4xqEXxl4LaDcz2txCQGid86ZRyZD6Ms

5c6W9FISbVlx6dOMxrenY5sJFmxPGAxoBCncVB5XGmxnDnYcEji7QH0dSTWgrSZ4nX/Wn3sO89gvaL2S9svYhAK9qvZr241shkoSEPLBDKUOdo5biTgcTdn2p1IaAKJnNIdJOfrkAiFbi8oV51tpnZLPtet2gpqcRnFX6DdlckbBpE+MYeUfilu9o6rwK89d2H3YgheAiOKM8hj5FVGO9kqtAaDQcb3cWbDxXbfjLN1h33NbyUxBdyndmm/jSPHx

18ouAT9RelIAjRzTe0GiDhQL02lTrJcM2XmmEZ0CjPGdD1WrN3yB2dIYSlTps6WHqynauuDIpYXnN56o2IzTALXt0FxBgTv6ulgQ9BhFxSvy4pRDg3IYnu0yQ+J3IY05YzD82CnaQ7syhQ7UW43JLcSH0AbluRBfgVmKLaBgZEGQAKh2M/jPLYRM+TOzD0Tla23emmo4Q5hMxaHdZM6LsbyYz5EDjOEzvcCTOUzvwxcXsy9zOPd9xtpOtwN1zpO9

mE9uRRB01eIrsU3Pph4apyx1MYAhAVkeM/dhTwaEE4hnAZuvX9DwToGhBFgRuBL3HtlSJe3Aitrtb3Kj8rMBhecnVRXFDos0DY7CmzMECjLTIHBw2Vk8fe6OFcthYRZqJbTBXaxy9UXuITRerW89kbS4YbSPZC/FIcvThRONoOR89ol9L2o/e0LeXU/c0UeAegE4gYATAF7BmC2WWHXOq1l2UmsO8nYcbQz4MSgOfF9Kc7PCeQMztAcDRTahMBzo

qb1xoL2C/guVz5ZIrN9Nsg8VWPt9vYpCbgmlhM97lL5ugHylwrqJZwNrdoxmODxwfnay060Ca4ROl04x3cfHCXGbU9/adx3hFsQ4J3pFv082OlZEbumAID5RbiHVFs8P3KVDq8P0gnwEjN5AMgdAGiYXyp3GEAXbZ7uMv2hbM6dxDFjgOMWIK0xa63vevSZHOxzic6nOZzwgDnOFzpc8KOeqUs+/DLLwy6p7EAWy7rOUuzbfCPttzzIPH112PeJV

xG7dcvEtjOiV+JcO5EGU38QaMlXB9ATQGYHfgRYH0AgcmAEbh1kX4BeBsAUHGovntvBZBH6LvQednPt7nLFZrVOcORwhfLHG1WfK2i3Xh5jLswIlzT/AUmmrTsOpc2Xq+UXODJgRVncV21Lpbx5pwsn2C9Yjojfkv85k83ZtJrS80THsg2awva9SggfEH+RrcERElSX1GCdxR5qIpauYOwvy8NL+Uf5PBqhNuJYNmgRBzB4zJ63uZdmnaVIvc2rY

DOvkdIwEuu6r6/VVPSD8o4YuKDqo84pJgJElzA60OvGpZglbNJhF+rgPbngECgS4haIdya9nlXBymy6WPBzXIFCNQb2PmPZL5kdzn8kOndPMGd3a9Lmkxw/akOWJu65/xBonY7SDRk8M50vbu6M/yhCY6uDgB/u6fibHlxqIW8Yu8lPP8EqxxJlWKKhsIAdgYAJ2FFvGxzhWbHJbuIUDzZb+W9kMxt1Ph7GimPM/a3+hzrcOKhxi+FyuV5gq6KuS

rsq4quqrmq/uGgrhxfY1lb1W/9gxbjW4lvEmaW6J6OAOW+8YFbqK422jhrbZOG2DJGG2A4AcHSiBTgGDGgAywavnp5BINkgYBoXCgBGJjVr0EdcX1PYH4IRAL7Bh60gVEBujoNgu9eQhIPJFOB9AbO6c2Jr81ULvq7gTFru6NE0dHZm74u9ruy7nBciwu7mu9Lvq5Q/oHvW7tIEbgobyuyLvB71fqM3aFae7Hv9AB8NhrlDnoFHvCxNu/i3oa9e5

Lv9AVQiNuxNHe57uTdzE/wIj7tIF+BsTmSzXvmAAQldBIQasHG0FEG+qkpNdG+7vukQBp3RMMEVKQALwYPpGxs17mroMBDZBgAIAO4Q5W9V7EkAbzxz7/QAnuQt0je/57eEgA3SUOFB5xH1lCAEh0XbL0GhA5SAh5VhQl5uGUB9IQSC9B/gSh8OAiH/JzXuq7r7F7vCQdp2DhOALtIalAgMwGEBmAN4ECJiANB5945E5uB3gqtlZd7EcM4IDkgYr

7ACIAllGK6ych8nkHrhu4Vxe6iXtNNCeFdmZgGRBgiOACUcNgS+/Efj4DInAArIYo3CAnEWPG/AgAA==
```
%%