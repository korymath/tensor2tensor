# coding=utf-8
# Copyright 2018 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests of basic flow of collecting trajectories and training PPO."""

# Dependency imports

from tensor2tensor.rl import rl_trainer_lib
from tensor2tensor.utils import trainer_lib

import tensorflow as tf


class TrainTest(tf.test.TestCase):

  def test_no_crash_pendulum(self):
    hparams = trainer_lib.create_hparams("pendulum_base", "epochs_num=10")
    rl_trainer_lib.train(hparams, "Pendulum-v0")

  def test_no_crash_cartpole(self):
    hparams = trainer_lib.create_hparams("cartpole_base", "epochs_num=10")
    rl_trainer_lib.train(hparams, "CartPole-v0")


if __name__ == "__main__":
  tf.test.main()
