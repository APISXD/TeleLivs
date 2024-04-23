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

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class BrandRegistrationOtpInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Brand Registration resource.
    :ivar brand_registration_sid: The unique string to identify Brand Registration of Sole Proprietor Brand
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], brand_registration_sid: str
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.brand_registration_sid: Optional[str] = payload.get(
            "brand_registration_sid"
        )

        self._solution = {
            "brand_registration_sid": brand_registration_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.BrandRegistrationOtpInstance {}>".format(context)


class BrandRegistrationOtpList(ListResource):

    def __init__(self, version: Version, brand_registration_sid: str):
        """
        Initialize the BrandRegistrationOtpList

        :param version: Version that contains the resource
        :param brand_registration_sid: Brand Registration Sid of Sole Proprietor Brand.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "brand_registration_sid": brand_registration_sid,
        }
        self._uri = "/a2p/BrandRegistrations/{brand_registration_sid}/SmsOtp".format(
            **self._solution
        )

    def create(self) -> BrandRegistrationOtpInstance:
        """
        Create the BrandRegistrationOtpInstance


        :returns: The created BrandRegistrationOtpInstance
        """

        payload = self._version.create(
            method="POST",
            uri=self._uri,
        )

        return BrandRegistrationOtpInstance(
            self._version,
            payload,
            brand_registration_sid=self._solution["brand_registration_sid"],
        )

    async def create_async(self) -> BrandRegistrationOtpInstance:
        """
        Asynchronously create the BrandRegistrationOtpInstance


        :returns: The created BrandRegistrationOtpInstance
        """

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
        )

        return BrandRegistrationOtpInstance(
            self._version,
            payload,
            brand_registration_sid=self._solution["brand_registration_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.BrandRegistrationOtpList>"