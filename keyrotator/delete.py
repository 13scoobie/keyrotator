# -*- coding: utf-8 -*-
# Copyright 2016 Google Inc. All Rights Reserved.
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
"""keyrotator Delete command."""

import iam_service


class DeleteCommand(object):
  """Implementation of the keyrotator delete commmand."""

  def run(self, project_id, iam_account, key_id):
    """Runs the delete command for keyrotator."""
    iam_service.delete_key(project_id, iam_account, key_id)

    print "Key successfully deleted."
    return 0
