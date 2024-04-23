r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class LinkshorteningMessagingServiceInstance(InstanceResource):
    """
    :ivar domain_sid: The unique string identifies the domain resource
    :ivar messaging_service_sid: The unique string that identifies the messaging service
    :ivar url:
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        domain_sid: Optional[str] = None,
        messaging_service_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.domain_sid: Optional[str] = payload.get("domain_sid")
        self.messaging_service_sid: Optional[str] = payload.get("messaging_service_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "domain_sid": domain_sid or self.domain_sid,
            "messaging_service_sid": messaging_service_sid
            or self.messaging_service_sid,
        }
        self._context: Optional[LinkshorteningMessagingServiceContext] = None

    @property
    def _proxy(self) -> "LinkshorteningMessagingServiceContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: LinkshorteningMessagingServiceContext for this LinkshorteningMessagingServiceInstance
        """
        if self._context is None:
            self._context = LinkshorteningMessagingServiceContext(
                self._version,
                domain_sid=self._solution["domain_sid"],
                messaging_service_sid=self._solution["messaging_service_sid"],
            )
        return self._context

    def create(self) -> "LinkshorteningMessagingServiceInstance":
        """
        Create the LinkshorteningMessagingServiceInstance


        :returns: The created LinkshorteningMessagingServiceInstance
        """
        return self._proxy.create()

    async def create_async(self) -> "LinkshorteningMessagingServiceInstance":
        """
        Asynchronous coroutine to create the LinkshorteningMessagingServiceInstance


        :returns: The created LinkshorteningMessagingServiceInstance
        """
        return await self._proxy.create_async()

    def delete(self) -> bool:
        """
        Deletes the LinkshorteningMessagingServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the LinkshorteningMessagingServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.LinkshorteningMessagingServiceInstance {}>".format(
            context
        )


class LinkshorteningMessagingServiceContext(InstanceContext):

    def __init__(self, version: Version, domain_sid: str, messaging_service_sid: str):
        """
        Initialize the LinkshorteningMessagingServiceContext

        :param version: Version that contains the resource
        :param domain_sid: The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
        :param messaging_service_sid: A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "domain_sid": domain_sid,
            "messaging_service_sid": messaging_service_sid,
        }
        self._uri = "/LinkShortening/Domains/{domain_sid}/MessagingServices/{messaging_service_sid}".format(
            **self._solution
        )

    def create(self) -> LinkshorteningMessagingServiceInstance:
        """
        Create the LinkshorteningMessagingServiceInstance


        :returns: The created LinkshorteningMessagingServiceInstance
        """
        data = values.of({})

        payload = self._version.create(method="POST", uri=self._uri, data=data)

        return LinkshorteningMessagingServiceInstance(
            self._version,
            payload,
            domain_sid=self._solution["domain_sid"],
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    async def create_async(self) -> LinkshorteningMessagingServiceInstance:
        """
        Asynchronous coroutine to create the LinkshorteningMessagingServiceInstance


        :returns: The created LinkshorteningMessagingServiceInstance
        """
        data = values.of({})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data
        )

        return LinkshorteningMessagingServiceInstance(
            self._version,
            payload,
            domain_sid=self._solution["domain_sid"],
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    def delete(self) -> bool:
        """
        Deletes the LinkshorteningMessagingServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the LinkshorteningMessagingServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.LinkshorteningMessagingServiceContext {}>".format(
            context
        )


class LinkshorteningMessagingServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the LinkshorteningMessagingServiceList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(
        self, domain_sid: str, messaging_service_sid: str
    ) -> LinkshorteningMessagingServiceContext:
        """
        Constructs a LinkshorteningMessagingServiceContext

        :param domain_sid: The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
        :param messaging_service_sid: A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
        """
        return LinkshorteningMessagingServiceContext(
            self._version,
            domain_sid=domain_sid,
            messaging_service_sid=messaging_service_sid,
        )

    def __call__(
        self, domain_sid: str, messaging_service_sid: str
    ) -> LinkshorteningMessagingServiceContext:
        """
        Constructs a LinkshorteningMessagingServiceContext

        :param domain_sid: The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
        :param messaging_service_sid: A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
        """
        return LinkshorteningMessagingServiceContext(
            self._version,
            domain_sid=domain_sid,
            messaging_service_sid=messaging_service_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.LinkshorteningMessagingServiceList>"
