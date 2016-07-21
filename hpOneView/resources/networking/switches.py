# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future import standard_library

standard_library.install_aliases()

__title__ = 'Switches'
__version__ = '0.0.1'
__copyright__ = '(C) Copyright (2012-2016) Hewlett Packard Enterprise ' \
                ' Development LP'
__license__ = 'MIT'
__status__ = 'Development'

from hpOneView.resources.resource import ResourceClient


class Switches(object):
    URI = '/rest/switches'

    def __init__(self, con):
        self._connection = con
        self._client = ResourceClient(con, self.URI)

    def get_statistics(self, id_or_uri, port_name=''):
        """
        Gets statistics for a switch
        Args:
            id: ID of switch
            port_name: switch port number (optional)

        Returns: dict
        """
        uri = self._client.build_uri(id_or_uri) + "/statistics"

        if port_name:
            uri += "/" + port_name

        return self._client.get(uri)

    def get_all(self, start=0, count=-1, filter='', sort=''):
        """
        Gets a list of top of rack switches.

        Args:
            start:
                The first item to return, using 0-based indexing.
                If not specified, the default is 0 - start with the first available item.
            count:
                The number of resources to return. A count of -1 requests all the items.
                The actual number of items in the response may differ from the requested
                count if the sum of start and count exceed the total number of items, or
                if returning the requested number of items would take too long.
            filter:
                A general filter/query string to narrow the list of items returned. The
                default is no filter - all resources are returned.
            sort:
                The sort order of the returned data set. By default, the sort order is based
                on create time, with the oldest entry first.

        Returns:
            list: A list of rack switches

        """
        return self._client.get_all(start, count, filter=filter, sort=sort)

    def get(self, id_or_uri):
        """
        Gets a switch by ID or by uri
        Args:
            id_or_uri: Could be either the switch ID or uri

        Returns:
            dict: switch
        """
        return self._client.get(id_or_uri)

    def delete(self, resource, force=False, timeout=-1):
        """
        Deletes a migrated switch

        Args:
            resource (dict): object to delete
            force (bool):
                 If set to true the operation completes despite any problems with
                 network connectivity or errors on the resource itself. The default is false.
            timeout:
                Timeout in seconds. Wait task completion by default. The timeout does not abort the operation
                in OneView, just stops waiting for its completion.

        Returns:
            dict: Details of associated resource

        """
        return self._client.delete(resource, force=force, timeout=timeout)

    def get_environmental_configuration(self, id_or_uri):
        """
        Gets the environmental configuration for a switch.

        Args:
            id_or_uri: Could be either the resource id or uri

        Returns:
            dict: environmental configuration
        """
        uri = self._client.build_uri(id_or_uri) + "/environmentalConfiguration"
        return self._client.get(uri)

    def get_by(self, field, value):
        """
        Get all switches that match the filter
        The search is case insensitive

        Args:
            field: field name to filter
            value: value to filter

        Returns: dict

        """
        return self._client.get_by(field, value)
