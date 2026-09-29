# UJ Mapping — Reverse Index: service_id → impacted User Journeys

**Use this file first in Phase 0A.** Contains the blast radius index, UJ hierarchy, Confluence post-mortem coordinates, and per-service incident metadata.

Lookup: find `service_id` → read `impacted_uj_keys` + `war_room_slack_channels`.

```tsv
service_id	impacted_uj_keys	war_room_slack_channels
oneff	ecommerce-checkout,instore-create-connected-order	#cuj-ecomm-checkout-war-room,#cuj-instore-create-connected-order-war-room
onecheckout	ecommerce-checkout,instore-create-connected-order	#cuj-ecomm-checkout-war-room,#cuj-instore-create-connected-order-war-room
web-checkout	ecommerce-checkout	#cuj-ecomm-checkout-war-room
nfs-checkout	ecommerce-checkout	#cuj-ecomm-checkout-war-room
onepay-v2	ecommerce-checkout,instore-create-connected-order,instore-nominal-purchase	#cuj-ecomm-checkout-war-room,#cuj-instore-create-connected-order-war-room,#cuj-instore-nominal-purchase-war-room
onepay-v1	ecommerce-checkout	#cuj-ecomm-checkout-war-room
onewallet	ecommerce-checkout	#cuj-ecomm-checkout-war-room
onequotation	ecommerce-checkout,instore-create-connected-order	#cuj-ecomm-checkout-war-room,#cuj-instore-create-connected-order-war-room
onepromotion	ecommerce-checkout	#cuj-ecomm-checkout-war-room
dktff	ecommerce-checkout	#cuj-ecomm-checkout-war-room
geolook	ecommerce-checkout,instore-create-connected-order,cg-common	#cuj-ecomm-checkout-war-room,#cuj-instore-create-connected-order-war-room,#cg-prod-war-room
gifting-core-transactions	ecommerce-checkout,instore-nominal-purchase	#cuj-ecomm-checkout-war-room,#cuj-instore-nominal-purchase-war-room
gifting-core-admin	customerrelationship-customer-care-management	#cuj-customerrelationship-customer-care-management
cubeinstore	instore-create-connected-order,instore-common,instore-product-price-update-processing	#cuj-instore-create-connected-order-war-room,#it-in-store,#cuj-instore-product-price-update-processing
cubeinstore-application	instore-common	#it-in-store
cubeinstore-cart-customer-order-creation	instore-create-connected-order	#cuj-instore-create-connected-order-war-room
cubeinstore-catalogue-product-page	instore-create-connected-order	#cuj-instore-create-connected-order-war-room
cubeinstore-customer-management	instore-create-connected-order	#cuj-instore-create-connected-order-war-room
cubeinstore-goods-flow	instore-reception-processing,instore-common	#cuj-instore-reception-processing-war-room,#it-in-store
cubeinstore-payments	instore-common	#it-in-store
cubeinstore-order-management	instore-common	#it-in-store
cubeinstore-shopping-experiences	instore-common	#it-in-store
cubeinstore-second-life	instore-common	#it-in-store
cubeinstore-printing	instore-common	#it-in-store
cubeinstore-boss-store-safe-management	instore-common	#it-in-store
cubeinstore-dashboard	instore-common	#it-in-store
cubeinstore-commercial	instore-common	#it-in-store
retail-stock	instore-reception-processing,instore-reception-pre-processing,instore-common	#cuj-instore-reception-processing-war-room,#it-in-store
webpos-eu	instore-nominal-purchase,instore-product-price-update-processing,instore-common	#cuj-instore-nominal-purchase-war-room,#cuj-instore-product-price-update-processing,#it-in-store
identity	instore-create-connected-order,instore-nominal-purchase,cg-common	#cuj-instore-create-connected-order-war-room,#cuj-instore-nominal-purchase-war-room,#cg-prod-war-room
square	customerrelationship-customer-care-management	#cuj-customerrelationship-customer-care-management
square-cube	customerrelationship-customer-care-management	#cuj-customerrelationship-customer-care-management
onebooking	bcp-booking-funnel	#cuj-bcp-booking-funnel-war-room
onepartner	bcp-markeplace-partner-management,bcp-common	#cuj-bcp-marketplace-partner-war-room,#bcp-war_rooms
masterprice	instore-create-connected-order,bcp-common,instore-product-price-update-processing	#cuj-instore-create-connected-order-war-room,#bcp-war_rooms,#cuj-instore-product-price-update-processing
onecatalog	bcp-common	#bcp-war_rooms
onecomm	bcp-common	#bcp-war_rooms
oneinvoice	bcp-common	#bcp-war_rooms
oneom	bcp-common	#bcp-war_rooms
onetax	bcp-common	#bcp-war_rooms
onereturn	bcp-common	#bcp-war_rooms
posdata	bcp-common	#bcp-war_rooms
poslog-manager	bcp-common	#bcp-war_rooms
usergeneratedcontent	bcp-common	#bcp-war_rooms
activities	bcp-common	#bcp-war_rooms
oneprice	bcp-common	#bcp-war_rooms
pixl	bcp-common	#bcp-war_rooms
membership	cg-common	#cg-prod-war-room
marketingauto	cg-common	#cg-prod-war-room
personalization	cg-common	#cg-prod-war-room
myaccount	cg-common	#cg-prod-war-room
targeting	cg-common	#cg-prod-war-room
content	cg-common	#cg-prod-war-room
measure	cg-common	#cg-prod-war-room
purchase	cg-common	#cg-prod-war-room
pro	cg-common	#cg-prod-war-room
sport	cg-common	#cg-prod-war-room
login	cg-common	#cg-prod-war-room
icheck	cg-common	#cg-prod-war-room
consent	cg-common	#cg-prod-war-room
apex-stock	instore-create-connected-order	#cuj-instore-create-connected-order-war-room
onestore	instore-create-connected-order,instore-product-price-update-processing	#cuj-instore-create-connected-order-war-room,#cuj-instore-product-price-update-processing
paramethor	instore-reception-processing,instore-product-price-update-processing,instore-common	#cuj-instore-reception-processing-war-room,#cuj-instore-product-price-update-processing,#it-in-store
signeasy	instore-product-price-update-processing,instore-common	#cuj-instore-product-price-update-processing,#it-in-store
effitag	instore-product-price-update-processing,instore-common	#cuj-instore-product-price-update-processing,#it-in-store
retail-prices	instore-product-price-update-processing,instore-common	#cuj-instore-product-price-update-processing,#it-in-store
product-api	instore-create-connected-order	#cuj-instore-create-connected-order-war-room
```

---

# UJ Hierarchy — Forward Index: User Journey → Moments → Services

**Use this section in Phase 0A step 2** to enumerate all services at risk for each impacted UJ.

---

## ecommerce-checkout

War room: `#cuj-ecomm-checkout-war-room` | Owning service: `web-checkout`

| Moment key | Services |
|---|---|
| `ecommerce-checkout-display-cart-page` | `onecheckout`, `oneff`, `onequotation`, `web-checkout`, `nfs-checkout` |
| `ecommerce-checkout-manage-items-cart` | `onecheckout`, `web-checkout` |
| `ecommerce-checkout-manage-coupons-cart` | `onecheckout`, `onepromotion`, `onequotation`, `web-checkout` |
| `ecommerce-checkout-submit-cart-go-shipping` | `onecheckout`, `web-checkout` |
| `ecommerce-checkout-login` | `onecheckout`, `web-checkout` |
| `ecommerce-checkout-manage-coupons-checkout` | `web-checkout` |
| `ecommerce-checkout-manage-address` | `geolook` |
| `ecommerce-checkout-display-choose-delivery-options` | `onecheckout`, `oneff`, `onequotation`, `web-checkout` |
| `ecommerce-checkout-submit-delivery-option` | `dktff`, `onecheckout`, `oneff`, `onequotation`, `web-checkout` |
| `ecommerce-checkout-display-payment-methods` | `onecheckout`, `onepay-v2`, `onepay-v1`, `onewallet`, `web-checkout`, `gifting-core-transactions` |
| `ecommerce-checkout-submit-payment` | `onecheckout`, `onepay-v2`, `onepay-v1`, `onewallet`, `web-checkout`, `gifting-core-transactions` |
| `ecommerce-checkout-redirected-confirmation-page` | `web-checkout` |

---

## instore-create-connected-order

War room: `#cuj-instore-create-connected-order-war-room` | Owning service: `cubeinstore`

| Moment key | Services |
|---|---|
| `instore-create-connected-order-launch-cubeinstore-application` | `cubeinstore`, `cubeinstore-cart-customer-order-creation`, `onestore` |
| `instore-create-connected-order-search-product` | `cubeinstore`, `cubeinstore-catalogue-product-page`, `cubeinstore-cart-customer-order-creation`, `oneff`, `product-api` |
| `instore-create-connected-order-add-product-to-cart` | `cubeinstore`, `cubeinstore-catalogue-product-page`, `cubeinstore-cart-customer-order-creation`, `masterprice`, `onecheckout` |
| `instore-create-connected-order-manage-items-in-cart` | `cubeinstore`, `cubeinstore-cart-customer-order-creation`, `apex-stock`, `onecheckout`, `oneff`, `product-api`, `masterprice` |
| `instore-create-connected-order-identify-my-customer` | `cubeinstore`, `cubeinstore-customer-management`, `cubeinstore-cart-customer-order-creation`, `identity`, `geolook` |
| `instore-create-connected-order-associate-customer-to-cart` | `cubeinstore`, `cubeinstore-customer-management`, `cubeinstore-cart-customer-order-creation`, `identity`, `geolook`, `onecheckout`, `oneff` |
| `instore-create-connected-order-validate-cart` | `cubeinstore`, `cubeinstore-cart-customer-order-creation` |
| `instore-create-connected-order-choose-delivery-options` | `cubeinstore`, `cubeinstore-customer-management`, `cubeinstore-cart-customer-order-creation`, `onestore`, `onecheckout` |
| `instore-create-connected-order-submit-delivery-options` | `cubeinstore`, `cubeinstore-customer-management`, `cubeinstore-cart-customer-order-creation`, `onecheckout` |
| `instore-create-connected-order-confirm-billing-address` | `cubeinstore`, `cubeinstore-customer-management`, `cubeinstore-cart-customer-order-creation` |
| `instore-create-connected-order-choose-order-payment-method` | `cubeinstore`, `cubeinstore-cart-customer-order-creation`, `onequotation` |
| `instore-create-connected-order-submit-order-payment-method` | `cubeinstore`, `cubeinstore-cart-customer-order-creation`, `onequotation`, `onecheckout` |
| `instore-create-connected-order-submit-receive-qr-code` | `cubeinstore`, `cubeinstore-cart-customer-order-creation`, `onepay-v2`, `onecheckout` |

---

## instore-nominal-purchase

War room: `#cuj-instore-nominal-purchase-war-room` | Owning service: `webpos-eu`

| Moment key | Services |
|---|---|
| `instore-nominal-purchase-customer-scan-product-on-till` | `webpos-eu` |
| `instore-nominal-purchase-customer-identify` | `webpos-eu`, `identity` |
| `instore-nominal-purchase-customer-pay-by-card` | `webpos-eu` |
| `instore-nominal-purchase-customer-pay-by-gifting-card` | `webpos-eu`, `onepay-v2`, `gifting-core-transactions` |

---

## instore-reception-processing

War room: `#cuj-instore-reception-processing-war-room` | Owning service: `retail-stock`

| Moment key | Services |
|---|---|
| `instore-reception-processing-select-reception-menu` | `cubeinstore`, `cubeinstore-goods-flow`, `retail-stock`, `paramethor`, `onestore` |
| `instore-reception-processing-choose-truck-reception` | `cubeinstore`, `cubeinstore-goods-flow`, `retail-stock` |
| `instore-reception-processing-validate-truck-reception` | `cubeinstore`, `cubeinstore-goods-flow`, `retail-stock` |
| `instore-reception-processing-choose-truck-reception-method` | `cubeinstore`, `cubeinstore-goods-flow`, `retail-stock` |
| `instore-reception-processing-confirm-truck-reception-method` | `cubeinstore`, `cubeinstore-goods-flow`, `retail-stock` |
| `instore-reception-processing-add-truck-departure-time` | `cubeinstore`, `cubeinstore-goods-flow`, `retail-stock` |
| `instore-reception-processing-receive-reception-confirmation` | `cubeinstore`, `cubeinstore-goods-flow`, `retail-stock`, `paramethor`, `retail-prices` |

---

## instore-reception-pre-processing

War room: `#cuj-instore-reception-processing-war-room` | Owning service: `retail-stock`

| Moment key | Services |
|---|---|
| `instore-reception-pre-processing-reception-flow-with-headers-are-consumed` | `retail-stock` |
| `instore-reception-pre-processing-reception-details-are-loaded` | `retail-stock`, `paramethor` |

---

## instore-product-price-update-processing

War room: `#cuj-instore-product-price-update-processing` | Owning service: `retail-prices`

| Moment key | Services |
|---|---|
| `instore-product-price-update-processing-price-modification` | `retail-prices`, `masterprice`, `paramethor`, `onestore` |
| `instore-product-price-update-processing-price-change-is-accepted` | `retail-prices`, `paramethor` |
| `instore-product-price-update-processing-price-change-is-forwarded-to-point-of-sale` | `retail-prices`, `webpos-eu` |
| `instore-product-price-update-processing-price-change-is-forwarded-to-labels-producer-application` | `retail-prices`, `signeasy`, `effitag` |
| `instore-product-price-update-processing-price-change-is-forwarded-to-cubeinstore-application` | `retail-prices`, `cubeinstore` |

---

## instore-common

War room: `#it-in-store` | Cross-cutting — all in-store UJs

| Moment key | Services |
|---|---|
| `instore-common` | `cubeinstore-application`, `cubeinstore-dashboard`, `cubeinstore-commercial`, `cubeinstore-catalogue-product-page`, `cubeinstore-customer-management`, `cubeinstore-cart-customer-order-creation`, `cubeinstore-shopping-experiences`, `cubeinstore-payments`, `cubeinstore-second-life`, `cubeinstore-order-management`, `cubeinstore-goods-flow`, `cubeinstore-printing`, `cubeinstore-boss-store-safe-management`, `retail-stock`, `cubeinstore`, `webpos-eu`, `tagit`, `rfid-robot-metralabs`, `rfid-robot-robotics`, `greengate`, `rfid-upos`, `rfid-link`, `rfid-alarm`, `mygame`, `sales-performances`, `onestore`, `mybusiness`, `signeasy`, `paramethor`, `apex-stock`, `apex-order`, `apex-product`, `arbo-instore`, `fcs`, `stic`, `effitime`, `retail-prices`, `highlight` |

---

## bcp-booking-funnel

War room: `#cuj-bcp-booking-funnel-war-room` | Owning service: `onebooking`

| Moment key | Services |
|---|---|
| `bcp-booking-funnel` | `onebooking` |

---

## bcp-markeplace-partner-management

War room: `#cuj-bcp-marketplace-partner-war-room` | Owning service: `onepartner`

| Moment key | Services |
|---|---|
| `bcp-markeplace-partner-management` | `onepartner` |

---

## bcp-common

War room: `#bcp-war_rooms` | Cross-cutting — all BCP platform services

| Moment key | Services |
|---|---|
| `bcp-common` | `masterprice`, `onecatalog`, `onecomm`, `oneinvoice`, `oneom`, `onetax`, `onereturn`, `posdata`, `poslog-manager`, `onepartner`, `usergeneratedcontent`, `activities`, `oneprice`, `pixl` |

---

## cg-common

War room: `#cg-prod-war-room` | Cross-cutting — Customer Growth platform

| Moment key | Services |
|---|---|
| `cg-common` | `membership`, `marketingauto`, `personalization`, `myaccount`, `targeting`, `content`, `measure`, `purchase`, `geolook`, `pro`, `sport`, `login`, `identity`, `icheck`, `consent` |

---

## customerrelationship-customer-care-management

War room: `#cuj-customerrelationship-customer-care-management` | Owning service: `square`

| Moment key | Services |
|---|---|
| `customerrelationship-search-order` | `square`, `square-cube` |
| `customerrelationship-search-giftcard` | `gifting-core-admin` |

---

# Confluence Coordinates — UJ → Space + Parent Page

Used by Phase 3 of `incident-investigation` to scope post-mortem CQL queries.  
When `confluence_space_id` and `confluence_parent_id` are filled, Phase 3 uses scoped CQL (faster, fewer false positives).  
Values migrated from `uj_data.md` (wiki_pm_space_id / wiki_pm_parent_id), mapped via owning service per UJ.

| uj_key | confluence_space_id | confluence_parent_id | owning_service |
|---|---|---|---|
| `ecommerce-checkout` | 191399123 | 1722614070 | web-checkout |
| `instore-create-connected-order` | 191399123 | 2120319963 | cubeinstore |
| `instore-nominal-purchase` | 191399123 | 2120319963 | webpos-eu |
| `instore-reception-processing` | 191399123 | 2120319963 | retail-stock |
| `instore-reception-pre-processing` | 191399123 | 2120319963 | retail-stock |
| `instore-product-price-update-processing` | 191399123 | 2120319963 | retail-prices |
| `instore-common` | 191399123 | 2120319963 | cubeinstore |
| `bcp-booking-funnel` | 194970190 | 1373896978 | onebooking |
| `bcp-markeplace-partner-management` | 194970190 | 1374486907 | onepartner |
| `bcp-common` | 194970190 | | multiple — no single parent |
| `cg-common` | 184943365 | 184961474 | membership |
| `customerrelationship-customer-care-management` | 191399123 | 2120319963 | square |

---

# Service Metadata — Per-Service Incident Context

Used by Phase 3 for Confluence search aliases and Phase 1 for escalation context.  
Fields: `pagerduty_service` and `smax_service` are aliases for fallback text search. `team_slack_channel` is for the Recommended Actions escalation section.

```tsv
service_id	pagerduty_service	smax_service	team_slack_channel	criticality
oneff	CE-ONEFF	ONEFF	oneff	critical
onecheckout	CE-ONECHECKOUT	ONECHECKOUT	onecheckout-public	critical
web-checkout	CE-WEB-CHECKOUT	WEB-CHECKOUT	ecomm-web-checkout-public	critical
nfs-checkout	CE-CUBE-FRONT	NFS-CHECKOUT	ecomm-front-squad-checkout	critical
onepay-v2	CE-ONEPAY-V2	ONEPAY-V2	bcp-payment-public	critical
onepay-v1		ONEPAY-V1	bcp-payment-public	high
onewallet	CE-ONEPAY-V2	ONEWALLET	bcp-payment-public	medium
onequotation	CE-ONEQUOTATION	ONEQUOTATION	onequotation-public	high
onepromotion	CE-ONEPROMOTION	ONEPROMOTION	onepromotion-public	high
dktff		DKT-FF-SAP-FF		critical
geolook	CE-MEMBER-GEOLOCATION	MEMBER-GEOLOOK	cg-geolocation-support	critical
cubeinstore	CubeInStore CE-INSTORE	CUBEINSTORE	cis-incident-broadcast	critical
webpos-eu	CS-WEBPOS-EU	WEBPOS-EU	webpos_eu_incident	critical
retail-stock	CS-RETAIL-STOCK	RETAIL-STOCK	stock-datadog	critical
identity	CE-MEMBER-IDENTITY	MEMBER-IDENTITY	cg-identity-support	critical
square	CE-SQUARE	SQUARE	square-production-support	high
square-cube	CE-SQUARE	SQUARE-CUBE	square-production-support	high
onebooking		ONE_BOOKING	dcp-onebooking-alerting-pr	medium
onepartner		ONE PARTNER	dcp-onepartner-support	medium
masterprice	CE-MASTERPRICE	MASTERPRICE	onesuite-masterprice-public	high
onecatalog		ONECATALOG	one-catalog-public	high
onecomm		ONECOMM	dcp-onepartner-support	medium
oneinvoice	CS-CUSTOMER_INVOICE	ONEINVOICE	oneinvoice-public	medium
oneom		ONEOM	oneom-public	medium
onetax	CE-ONETAX	ONETAX	onetax-public	medium
onereturn		ONERETURN	onereturn	medium
posdata		POSDATA	posdata-public	medium
poslog-manager		POSLOG-MANAGER	posdata-public	medium
usergeneratedcontent		REVIEWS		high
activities		DECATHLON ACTIVITIES	dcp-activities-support	medium
oneprice	CE-ONEPRICE	ONEPRICE	onesuite-masterprice-public	medium
pixl		MEDIA_PIXL		medium
membership	CE-MEMBERSHIP	UNITED-MEMBERSHIP-PROGRAM	cr-membership-teams	high
marketingauto	CE-MARTECH-MARKETING-AUTO	MARTECH-MARKETING-AUTOMATION	martech-team-mka	critical
personalization	CE-MARTECH-PERSONALIZATION	MARTECH-API-RECO		low
myaccount	CE-MEMBER-MYACCOUNT	MEMBER-MYACCOUNT		critical
targeting	CE-MARTECH-CAMPAIGN-MKT	MARTECH-IDELIVER		medium
content	CE-MARTECH-CONTENT	MARTECH-IDELIVER		medium
measure	CE-MARTECH-MEASURE	MARTECH-IDELIVER		low
login	CE-MEMBER-LOGIN	MEMBER-LOGIN	cg-login	critical
icheck	CE-MEMBER-ICHECK	MEMBER-ICHECK	member-icheck	critical
consent	CE-MEMBER-CONSENTS	MEMBER-CONSENTS	cg-consent	critical
sport	CE-MEMBER-SPORT	MEMBER-SPORT-HUB	cg-sport-public	medium
pro	CE-MEMBER-PRO	MEMBER-PRO	member-pro-public	medium
purchase	CE-MEMBER-PURCHASE	MEMBER-PURCHASES	member-purchase-consumer	medium
onestore	CS-ONESTORE	ONESTORE	mybusiness-prod	high
product-api	CS-XMERCH-SKU	XMERCH-PRODUCTAPI	ecomm-product-api-public	critical
```
