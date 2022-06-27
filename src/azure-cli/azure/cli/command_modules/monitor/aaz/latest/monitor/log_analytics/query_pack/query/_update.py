# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "monitor log-analytics query-pack query update",
    is_preview=True,
)
class Update(AAZCommand):
    """Update a specific query within a log analytics query pack.

    :example: Update a query in a query pack
        az monitor log-analytics query-pack query update --query-id 112c6b1f-5a86-4f01-a2d7-efb8e31f930f -g resourceGroup  --query-pack-name queryPackName --body "heartbeat | take 20" --categories [2]=databases --tags version[0]=null
    """

    _aaz_info = {
        "version": "2019-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/querypacks/{}/queries/{}", "2019-09-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.query_id = AAZStrArg(
            options=["-n", "--name", "--query-id"],
            help="The id name of a specific query defined in the log analytics query pack. It must be of type GUID.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.query_pack_name = AAZStrArg(
            options=["--query-pack-name"],
            help="The name of the log analytics query pack.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.body = AAZStrArg(
            options=["--body"],
            arg_group="Properties",
            help="Content of the query.",
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="Description of the query.",
            nullable=True,
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="Unique display name for your query within the query pack.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Properties",
            help="Tags associated with the query.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZListArg(
            nullable=True,
        )

        _element = cls._args_schema.tags.Element
        _element.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Related"

        _args_schema = cls._args_schema
        _args_schema.categories = AAZListArg(
            options=["--categories"],
            arg_group="Related",
            help={"short-summary": "The related categories for the function.", "long-summary": "Supported value are: `security`, `network`, `management`, `virtualmachines`, `container`, `audit`, `desktopanalytics`, `workloads`, `resources`, `applications`, `monitor`, `databases`, `windowsvirtualdesktop` etc."},
            nullable=True,
        )
        _args_schema.resource_types = AAZListArg(
            options=["--resource-types"],
            arg_group="Related",
            help="The related resource types for the function.",
            nullable=True,
        )
        _args_schema.solutions = AAZListArg(
            options=["--solutions"],
            arg_group="Related",
            help="The related Log Analytics solutions for the function.",
            nullable=True,
        )

        categories = cls._args_schema.categories
        categories.Element = AAZStrArg(
            nullable=True,
        )

        resource_types = cls._args_schema.resource_types
        resource_types.Element = AAZStrArg(
            nullable=True,
        )

        solutions = cls._args_schema.solutions
        solutions.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.QueriesGet(ctx=self.ctx)()
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.QueriesPut(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class QueriesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "id", self.ctx.args.query_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "queryPackName", self.ctx.args.query_pack_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_log_analytics_query_pack_query_read(cls._schema_on_200)

            return cls._schema_on_200

    class QueriesPut(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "id", self.ctx.args.query_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "queryPackName", self.ctx.args.query_pack_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_log_analytics_query_pack_query_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("body", AAZStrType, ".body", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("displayName", AAZStrType, ".display_name", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("related", AAZObjectType)
                properties.set_prop("tags", AAZDictType, ".tags")

            related = _builder.get(".properties.related")
            if related is not None:
                related.set_prop("categories", AAZListType, ".categories")
                related.set_prop("resourceTypes", AAZListType, ".resource_types")
                related.set_prop("solutions", AAZListType, ".solutions")

            categories = _builder.get(".properties.related.categories")
            if categories is not None:
                categories.set_elements(AAZStrType, ".")

            resource_types = _builder.get(".properties.related.resourceTypes")
            if resource_types is not None:
                resource_types.set_elements(AAZStrType, ".")

            solutions = _builder.get(".properties.related.solutions")
            if solutions is not None:
                solutions.set_elements(AAZStrType, ".")

            tags = _builder.get(".properties.tags")
            if tags is not None:
                tags.set_elements(AAZListType)

            _elements = _builder.get(".properties.tags{}")
            if _elements is not None:
                _elements.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


_schema_log_analytics_query_pack_query_read = None


def _build_schema_log_analytics_query_pack_query_read(_schema):
    global _schema_log_analytics_query_pack_query_read
    if _schema_log_analytics_query_pack_query_read is not None:
        _schema.id = _schema_log_analytics_query_pack_query_read.id
        _schema.name = _schema_log_analytics_query_pack_query_read.name
        _schema.properties = _schema_log_analytics_query_pack_query_read.properties
        _schema.system_data = _schema_log_analytics_query_pack_query_read.system_data
        _schema.type = _schema_log_analytics_query_pack_query_read.type
        return

    _schema_log_analytics_query_pack_query_read = AAZObjectType()

    log_analytics_query_pack_query_read = _schema_log_analytics_query_pack_query_read
    log_analytics_query_pack_query_read.id = AAZStrType(
        flags={"read_only": True},
    )
    log_analytics_query_pack_query_read.name = AAZStrType(
        flags={"read_only": True},
    )
    log_analytics_query_pack_query_read.properties = AAZObjectType(
        flags={"required": True},
    )
    log_analytics_query_pack_query_read.system_data = AAZObjectType(
        serialized_name="systemData",
        flags={"read_only": True},
    )
    log_analytics_query_pack_query_read.type = AAZStrType(
        flags={"read_only": True},
    )

    properties = _schema_log_analytics_query_pack_query_read.properties
    properties.author = AAZStrType(
        flags={"read_only": True},
    )
    properties.body = AAZStrType(
        flags={"required": True},
    )
    properties.description = AAZStrType()
    properties.display_name = AAZStrType(
        serialized_name="displayName",
        flags={"required": True},
    )
    properties.id = AAZStrType(
        flags={"read_only": True},
    )
    properties.related = AAZObjectType()
    properties.tags = AAZDictType()
    properties.time_created = AAZStrType(
        serialized_name="timeCreated",
        flags={"read_only": True},
    )
    properties.time_modified = AAZStrType(
        serialized_name="timeModified",
        flags={"read_only": True},
    )

    related = _schema_log_analytics_query_pack_query_read.properties.related
    related.categories = AAZListType()
    related.resource_types = AAZListType(
        serialized_name="resourceTypes",
    )
    related.solutions = AAZListType()

    categories = _schema_log_analytics_query_pack_query_read.properties.related.categories
    categories.Element = AAZStrType()

    resource_types = _schema_log_analytics_query_pack_query_read.properties.related.resource_types
    resource_types.Element = AAZStrType()

    solutions = _schema_log_analytics_query_pack_query_read.properties.related.solutions
    solutions.Element = AAZStrType()

    tags = _schema_log_analytics_query_pack_query_read.properties.tags
    tags.Element = AAZListType()

    _element = _schema_log_analytics_query_pack_query_read.properties.tags.Element
    _element.Element = AAZStrType()

    system_data = _schema_log_analytics_query_pack_query_read.system_data
    system_data.created_at = AAZStrType(
        serialized_name="createdAt",
        flags={"read_only": True},
    )
    system_data.created_by = AAZStrType(
        serialized_name="createdBy",
        flags={"read_only": True},
    )
    system_data.created_by_type = AAZStrType(
        serialized_name="createdByType",
        flags={"read_only": True},
    )
    system_data.last_modified_at = AAZStrType(
        serialized_name="lastModifiedAt",
        flags={"read_only": True},
    )
    system_data.last_modified_by = AAZStrType(
        serialized_name="lastModifiedBy",
        flags={"read_only": True},
    )
    system_data.last_modified_by_type = AAZStrType(
        serialized_name="lastModifiedByType",
        flags={"read_only": True},
    )

    _schema.id = _schema_log_analytics_query_pack_query_read.id
    _schema.name = _schema_log_analytics_query_pack_query_read.name
    _schema.properties = _schema_log_analytics_query_pack_query_read.properties
    _schema.system_data = _schema_log_analytics_query_pack_query_read.system_data
    _schema.type = _schema_log_analytics_query_pack_query_read.type


__all__ = ["Update"]
