# fakeuseragent
Repository fix [fake-useragent](https://github.com/fake-useragent/) for windows.

Up-to-date simple useragent faker with real world database.

## Features

- Data is pre-downloaded from [useragentstring.com](http://useragentstring.com/) and part of the package
- Retrieves user-agent strings locally

### Usage

```py
import fakeuseragent

fa = fakeuseragent.UserAgent()

fa.random
# Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.6)
fa.ie
# Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)
fa.msie
# Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8; .NET4.0C; .NET4.0E; InfoPath.3)
fa.chrome
# Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19
fa.safari
# Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16
fa.edge
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246
fa.ff
# Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.7.13) Gecko/20060418 Firefox/1.0.8 (Ubuntu package 1.0.8)
fa.firefox
# Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070719 CentOS/1.5.0.12-0.3.el4.centos Firefox/1.5.0.12
fa.googlechrome
# Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13
fa.internetexplorer
# Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6; Hotbar 3.0)
fa.opera
# Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.4-4GB i686) Opera 5.0  [en]
```
By default `fakeuseragent` will use it's local ([`browsers.json`](browsers.json)) data file as the data source.

If you don't want to use the local data, but use the external data source to retrieve the user-agents. Set `use_external_data` to `True`:

```py
from fakeuseragent import UserAgent
file_path = 'C:\\test\\fakeuseragent\\browsers.json'
fa = UserAgent(use_external_data=True, cache_path=file_path)
fa.random
#Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8
```

### Changelog
- 1.1.1001 
  - More correctly composed ([`browsers.json`](browsers.json))
  - Version system removed

### [Authors page](https://github.com/fake-useragent/fake-useragent/blob/master/AUTHORS)

