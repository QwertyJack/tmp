[![CircleCI](https://circleci.com/gh/QwertyJack/tmp/tree/master.svg?style=svg&circle-token=4b01597782d155122d4d48b4b56d002c2b2b3368)](https://circleci.com/gh/QwertyJack/tmp/tree/master)
[![Build Status](https://travis-ci.org/QwertyJack/tmp.svg?branch=master)](https://travis-ci.org/QwertyJack/tmp)

# CI Example

Python 集成测试建议

- 有一个相对清晰的包结构和目录树，例如 [`my`](my)，更多内容参考：
    + [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
    + [Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)
- 用 [virtualenv](https://virtualenv.pypa.io/en/latest/) 和 [`requirements.txt`](requirements.txt) 管理依赖
- 使用静态检查 [Flake8](http://flake8.pycqa.org/en/latest/), 可以参考[我的配置文件](.flake8)

  安装: `pip install flake8`

  使用方法: `flake8`

- 写单元/集成测试，测试框架使用 [pytest](https://docs.pytest.org/en/latest/), 参考 [`tests`](tests)
- 使用 CI 服务(点本文上边的绿框):
    + [CircleCI](https://circleci.com/): 免费版提供 4 个容器(最多同时构建 4 个任务), 资源 2c4g
    + [Travis CI](https://travis-ci.org): 免费版最多同时构建 ? 个任务，资源 2c8g
    + [Actions](https://github.com/features/actions): Github 最近上线的 CI/CD 服务，目前处于 beta 公测阶段
