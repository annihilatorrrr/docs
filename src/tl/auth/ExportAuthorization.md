# auth.ExportAuthorization

Returns data for copying authorization to another data-centre.



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.auth.ExportAuthorization({
    dcId: 43
}));
    console.log(result); // prints the result
})();
```
:::

:::tab{title="TypeScript"}
```ts
import {Api, TelegramClient} from 'telegram';
import {StringSession} from 'telegram/sessions';

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result: Api.auth.ExportedAuthorization = await client.invoke(new Api.auth.ExportAuthorization({
    dcId: 43
}));
    console.log(result); // prints the result
})();
```
:::
::::



## Parameters

| Name | Type | Description |
| :--: | ---- | ----------- |
| **dcId** | [int](https://core.telegram.org/type/int) | Number of a target data-centre 


## Result

[auth.ExportedAuthorization](https://core.telegram.org/type/auth.ExportedAuthorization)



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |
| 400 | DC\_ID\_INVALID | The provided DC ID is invalid 


## Can bots use this method?

Yes

## Related pages

