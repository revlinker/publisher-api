# Author: @pedroserrudo
# This is a sample Python script to use REVLINKER Publisher API

import requests

GET, POST = 'GET', 'POST'


class RevlinkerPUBAPI:
    api_key = None
    base_url = "https://pub.revlinker.com/api/v1/"
    client = None

    def __init__(self, api_key):
        self.api_key = api_key

    def set_api_key(self, api_key):
        self.api_key = api_key

    def request(self, url, params=None, data=None, method=GET):

        return requests.request(
            method=method,
            url=url,
            params=params,
            json=data,
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": self.api_key
            }
        ).json()

    def is_offer_active(self, offer_id=None, uuid=None):
        """
        :param receive offer_id or uuid
        :return: returns True if is activate, returns False if it's Inactive or something else
        """
        if offer_id:
            url = f'{self.base_url}offers/?status=1' + f'&id={offer_id}'
        elif uuid:
            url = f'{self.base_url}offers/?status=1' + f'&uuid={uuid}'
        else:
            raise 'No id provided'

        req = self.request(url)

        return len(req['results']) == 0

    def get_offers(self, params=None):
        """
        Available filters
        limit: Number of results to return per page.
        offset: The initial index from which to return the results.
        id: Filter by Offer ID
        uuid: filter by Offer UUID
        status: filter status
                1 - Active
                2,3 - Inactive
                4 - Active but Capped
        payout_model: filter by Offer Payout Model
                CPA, CPI, CPS, CPL, CPM, CPE, CPD
        search: Search term for offer name and description
        ordering: ordering field, payout, id, name, etc.. use - to invert
        :return: Json dict
        """

        url = f'{self.base_url}offers/'

        return self.request(url=url, params=params)

    def get_campaigns(self, params=None):
        """
        Available filters
        limit: Number of results to return per page.
        offset: The initial index from which to return the results.
        search: Search term for offer name and description
        ordering: ordering field id, name, status, etc... - to invert
        """

        url = f'{self.base_url}campaigns/'

        return self.request(url=url, params=params)

    def create_campaign(self, offer):
        """
        Receives Offer_id or offer_uuid and creates campaign,
        :return URL & status
        """
        url = f'{self.base_url}campaigns/'

        return self.request(method=POST, url=url, data={'offer': offer})


pubapi = RevlinkerPUBAPI('api_key')
