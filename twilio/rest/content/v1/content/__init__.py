r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Content
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.content.v1.content.approval_fetch import ApprovalFetchList


class ContentInstance(InstanceResource):
    """
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar sid: The unique string that that we created to identify the Content resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.
    :ivar friendly_name: A string name used to describe the Content resource. Not visible to the end recipient.
    :ivar language: Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in.
    :ivar variables: Defines the default placeholder values for variables included in the Content resource. e.g. {\"1\": \"Customer_Name\"}.
    :ivar types: The [Content types](https://www.twilio.com/docs/content/content-types-overview) (e.g. twilio/text) for this Content resource.
    :ivar url: The URL of the resource, relative to `https://content.twilio.com`.
    :ivar links: A list of links related to the Content resource, such as approval_fetch and approval_create
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.language: Optional[str] = payload.get("language")
        self.variables: Optional[Dict[str, object]] = payload.get("variables")
        self.types: Optional[Dict[str, object]] = payload.get("types")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[ContentContext] = None

    @property
    def _proxy(self) -> "ContentContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ContentContext for this ContentInstance
        """
        if self._context is None:
            self._context = ContentContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ContentInstance":
        """
        Fetch the ContentInstance


        :returns: The fetched ContentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ContentInstance":
        """
        Asynchronous coroutine to fetch the ContentInstance


        :returns: The fetched ContentInstance
        """
        return await self._proxy.fetch_async()

    @property
    def approval_fetch(self) -> ApprovalFetchList:
        """
        Access the approval_fetch
        """
        return self._proxy.approval_fetch

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ContentInstance {}>".format(context)


class ContentContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ContentContext

        :param version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Content/{sid}".format(**self._solution)

        self._approval_fetch: Optional[ApprovalFetchList] = None

    def delete(self) -> bool:
        """
        Deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ContentInstance:
        """
        Fetch the ContentInstance


        :returns: The fetched ContentInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ContentInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ContentInstance:
        """
        Asynchronous coroutine to fetch the ContentInstance


        :returns: The fetched ContentInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ContentInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def approval_fetch(self) -> ApprovalFetchList:
        """
        Access the approval_fetch
        """
        if self._approval_fetch is None:
            self._approval_fetch = ApprovalFetchList(
                self._version,
                self._solution["sid"],
            )
        return self._approval_fetch

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ContentContext {}>".format(context)


class ContentPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ContentInstance:
        """
        Build an instance of ContentInstance

        :param payload: Payload response from the API
        """
        return ContentInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1.ContentPage>"


class ContentList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ContentList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Content"

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ContentInstance]:
        """
        Streams ContentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ContentInstance]:
        """
        Asynchronously streams ContentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ContentInstance]:
        """
        Lists ContentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ContentInstance]:
        """
        Asynchronously lists ContentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ContentPage:
        """
        Retrieve a single page of ContentInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ContentInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ContentPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ContentPage:
        """
        Asynchronously retrieve a single page of ContentInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ContentInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ContentPage(self._version, response)

    def get_page(self, target_url: str) -> ContentPage:
        """
        Retrieve a specific page of ContentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ContentInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ContentPage(self._version, response)

    async def get_page_async(self, target_url: str) -> ContentPage:
        """
        Asynchronously retrieve a specific page of ContentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ContentInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ContentPage(self._version, response)

    def get(self, sid: str) -> ContentContext:
        """
        Constructs a ContentContext

        :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
        """
        return ContentContext(self._version, sid=sid)

    def __call__(self, sid: str) -> ContentContext:
        """
        Constructs a ContentContext

        :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
        """
        return ContentContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1.ContentList>"