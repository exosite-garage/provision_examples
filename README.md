================================================================================
Provision API Usage Examples
================================================================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These are examples of how to interact with Exosite's Provisioning API.  The
file "provision_test.py" shows a sequence for setting up, using, and then
tearing down the provisioning interface for a given VENDOR.

The management APIs assume you have your own Portals Whitebox at a URL like
<subdomain>.<domain>.com -> e.g. portals.exosite.com.

License is BSD, Copyright 2012, Exosite LLC (see LICENSE file)

Built/tested with Python 2.7

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Quick Start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Install python
  * http://www.python.org/download/
  * http://www.python.org/download/releases/2.7.2/

* Register for API keys on the One Platform by signing up for an Exosite Portals
  whitebox at https://portals.exosite.com.  You will need the following keys and
  information:
  * VENDORNAME -> get this on the /admin/provision page of a Portals instance
  * VENDORTOKEN -> same place
  * CLONERID -> create a client (device) in the Portals instance somewhere and
    check the box "Use as Clone" (or use the JSON RPC API to set it up)
  * OWNERCIK -> the easiest thing here is to use a Portal CIK - get this from
    a Portal listed on your /account/portals page

* After filling in the constants per above, run the script

    python provision_test.py

* Check the script output to get an understanding for how everything works.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
More Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Provision API Overview -> http://exosite.com/products/onep/documentation?cid=
  4523
* Provision API Reference -> http://exosite.com/products/onep/documentation?cid=
  5981

**Notes**

* The provisoining system is a powerful interface that allows a device OEM to
  deploy fleets of devices and for those devices to subsequently instantiate 
  themselves with the Exosite system.  When a device instantiates with its
  model's profile, you can have scripts automatically run to do things like
  provision on a cellular network, notify stakeholders of activity, begin a 
  billing process, enable additional features, etc...

