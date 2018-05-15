#!/usr/bin/env bash

set -o pipefail
set -o nounset


cmd="$1"
cmd_args="${@:2}"

function print_usage() {
  echo "usage: ./run.sh <command>"
  echo ""
  echo "Commands:"
  echo ""
  echo "help,-h,--help        show this help message and exit"
  echo "tests                 run tests and code coverage"
  echo "pep8                  check code against pep8"
  echo "rover                 execute Mars rover app"
  exit 1
}


case ${cmd} in
  help|--help|-h|'')
    print_usage
    ;;
  test|tests)
    docker run -t -v `pwd`:/app -v ~/.pdbrc.py:/root/.pdbrc.py -i --rm rover pytest -s ${cmd_args} --cov-report term-missing --cov=. 
    ;;
  pep8|flake8)
    docker run -t -v `pwd`:/app -v ~/.pdbrc.py:/root/.pdbrc.py -i --rm rover flake8 --statistics . ${cmd_args}
    ;;
  *)
    docker run -v `pwd`:/app -i --rm rover ${cmd} ${cmd_args}
    ;;
esac
