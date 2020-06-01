#!/usr/bin/env bats

load 'libs/bats-support/load'
load 'libs/bats-assert/load'

load test_helper

@test "Sourcing works, by checking if \$system is set" {
    run echo $system
    refute_output "MacOS"
}

@test "#get_themes populates themes" {
  get_themes
  assert_success
  assert [ ${#themes[@]} -gt 0 ]
}