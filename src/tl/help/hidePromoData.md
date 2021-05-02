# help.hidePromoData

Hide MTProxy/Public Service Announcement information

## Example

::::tabs
:::tab{title="JavaScript"}

```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.help.hidePromoData({
		peer: new Api.InputPeer({ /* ... */ }... */ }),
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
    const result: Api.Bool = await client.invoke(new Api.help.hidePromoData({
		peer: new Api.InputPeer({ /* ... */ }... */ }),
		}));
    console.log(result); // prints the result
})();
```

:::
::::

## TL schema

```txt
boolFalse#bc799737 = Bool;
boolTrue#997275b5 = Bool;
---functions---
help.hidePromoData#1e251c95 peer:InputPeer = Bool;
```

## Parameters

|   Name   | Type                                                  | Description  |
| :------: | ----------------------------------------------------- | ------------ |
| **peer** | [InputPeer](https://core.telegram.org/type/InputPeer) | Peer to hide |

## Result

[Bool](https://core.telegram.org/type/Bool)

## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |

## Can bots use this method?

Yes

## Related pages