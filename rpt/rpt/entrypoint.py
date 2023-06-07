# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Martin Constante
# All rights reserved.


def get_param_value(params: list, value: str) -> str:
    try:
        if params[0]['id'] == value:
            return params[0]['value']
        if len(params) == 1:
            return '-'
        return get_param_value(list(params[1:]), value)
    except Exception:
        return '-'


def generate(
    client=None,
    input_data=None,
    progress_callback=None,
    renderer_type='xlsx',
    extra_context_callback=None,
):
    total = client.requests.all().count()
    progress = 0
    yield (
        'Request ID',
        'Request Type',
        'Request Status',
        'Created At',
        'Updated At',
        'Customer ID',
        'Customer Name',
        'Customer External ID',
        'Tier 1 ID',
        'Tier 1 Name',
        'Tier 1 External ID',
        'Tier 2 ID',
        'Tier 2 Name',
        'Tier 2 External ID',
        'Marketplace ID',
        'Marketplace Name',
        'Provider ID',
        'Provider Name',
        'Vendor ID',
        'Vendor Name',
        'Product ID',
        'Product Name',
        'Asset ID',
        'Asset External ID',
        'Hub ID',
        'Hub Name',
        'MPN',
        'Units',
        'Company ID',
        'License Start Date',
        'License End Date',
        'Subscription ID'
    )
    for request in client.requests.all():
    # for request in client.requests.filter(status__in=('pending', 'approved', 'failed')):
        parameters_list = request['asset']['params']
        companyID = get_param_value(parameters_list, 'companyID')
        licenseStartDate = get_param_value(parameters_list, 'licenseStartDate')
        licenseEndDate = get_param_value(parameters_list, 'licenseEndDate')
        subscriptionID = get_param_value(parameters_list, 'subscriptionID')
        for item in request['asset']['items']:
            yield (
                request['id'],
                request['type'],
                request['status'],
                request['events']['created']['at'],
                request['events']['updated']['at'],
                request['asset']['tiers']['customer']['id'],
                request['asset']['tiers']['customer']['name'],
                request['asset']['tiers']['customer']['external_id'],
                request['asset']['tiers']['tier1']['id'],
                request['asset']['tiers']['tier1']['name'],
                request['asset']['tiers']['tier1']['external_id'],
                request['asset']['tiers']['tier1']['id'],
                request['asset']['tiers']['tier1']['name'],
                request['asset']['tiers']['tier1']['external_id'],
                request['marketplace']['id'],
                request['marketplace']['name'],
                request['asset']['connection']['provider']['id'],
                request['asset']['connection']['provider']['name'],
                request['asset']['connection']['vendor']['id'],
                request['asset']['connection']['vendor']['name'],
                request['asset']['product']['id'],
                request['asset']['product']['name'],
                request['asset']['id'],
                request['asset']['external_id'],
                request['asset']['connection']['hub']['id'],
                request['asset']['connection']['hub']['name'],
                item['mpn'],
                item['quantity'],
                companyID,
                licenseStartDate,
                licenseEndDate,
                subscriptionID
            )
        progress += 1
        progress_callback(progress, total)
