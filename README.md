# REVLINKER Publisher API - Python

## Install
```bash
pip install https://github.com/revlinker/publisher-api/archive/refs/heads/master.zip
```

## Usage
```bash
from revlinker import pubapi

# Set API Key
pubapi.set_api_key('api_key')

# Get Offers
pubapi.get_offers({'limit':1000})

# Get Campaigns
pubapi.get_campaigns({'limit':1000})

# Is Offer Active 
pubapi.is_offer_active('{{uuid|offer_id}}')

# Create Campaign
pubapi.create_campaign('{{uuid|offer_id}}')
```

Get your API key here [pub.revlinker.com/api/key](https://pub.revlinker.com/api/key)


