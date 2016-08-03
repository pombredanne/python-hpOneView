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

from pprint import pprint

from config_loader import try_load_from_file
from hpOneView.oneview_client import OneViewClient

config = {
    "ip": "<oneview_ip>",
    "credentials": {
        "userName": "<oneview_administrator_name>",
        "password": "<oneview_administrator_password>",
    }
}

server_profile_name = "Profile101"
server_hardware_type_uri = "/rest/server-hardware-types/C8DEF9A6-9586-465E-A951-3070988BC226"
enclosure_group_uri = "/rest/enclosure-groups/a0f1c07b-f811-4c85-8e38-ac5ec34ea2f4"

# Try load config from a file (if there is a config file)
config = try_load_from_file(config)

oneview_client = OneViewClient(config)

# Create a server profile
print("\nCreate a basic connection-less assigned server profile")
basic_profile_options = dict(
    name=server_profile_name,
    serverHardwareTypeUri=server_hardware_type_uri,
    enclosureGroupUri=enclosure_group_uri
)
basic_profile = oneview_client.server_profiles.create(basic_profile_options)
pprint(basic_profile)

# Update bootMode from recently created profile
print("\nUpdate bootMode from recently created profile")
profile_to_update = basic_profile.copy()
profile_to_update["bootMode"] = dict(manageMode=True, mode="BIOS")
profile_updated = oneview_client.server_profiles.update(resource=profile_to_update, id_or_uri=profile_to_update["uri"])
pprint(profile_updated)

# Get all
print("\nGet list of all server profiles")
all_profiles = oneview_client.server_profiles.get_all()
for profile in all_profiles:
    print('  %s' % profile['name'])

# Get by property
print("\nGet a list of server profiles that matches the specified macType")
profile_mac_type = all_profiles[1]["macType"]
profiles = oneview_client.server_profiles.get_by('macType', profile_mac_type)
for profile in profiles:
    print('  %s' % profile['name'])

# Get by name
print("\nGet a server profile by name")
profile = oneview_client.server_profiles.get_by_name(server_profile_name)
pprint(profile)

# Get by uri
print("\nGet a server profile by uri")
profile_uri = all_profiles[0]["uri"]
profile = oneview_client.server_profiles.get(profile_uri)
pprint(profile)

# Delete the created server profile
print("\nDelete the created server profile")
oneview_client.server_profiles.delete(basic_profile)
print("The server profile was successfully deleted.")