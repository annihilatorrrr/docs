# messages.reorderStickerSets

Reorder installed stickersets

## Example

::::tabs
:::tab{title="JavaScript"}

```js
const { Api, TelegramClient } = require('telegram');
const { StringSession } = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(
        new Api.messages.reorderStickerSets({
            masks: true,
            order: [6554686],
        }),
    );
    console.log(result); // prints the result
})();
```

:::

:::tab{title="TypeScript"}

```ts
import { Api, TelegramClient } from 'telegram';
import { StringSession } from 'telegram/sessions';

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result: Api.Bool = await client.invoke(
        new Api.messages.reorderStickerSets({
            masks: true,
            order: [6554686],
        }),
    );
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
messages.reorderStickerSets#78337739 flags:# masks:flags.0?true order:Vector<long> = Bool;
```

## Parameters

|   Name    | Type                                                                                                                              | Description                                                                                             |
| :-------: | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **flags** | [#](https://core.telegram.org/type/%23)                                                                                           | Flags, see [TL conditional fields](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) |
| **masks** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).0?[true](https://core.telegram.org/constructor/true) | Reorder mask stickersets                                                                                |
| **order** | [Vector](https://core.telegram.org/type/Vector%20t) < [long](https://core.telegram.org/type/long) >                               | New stickerset order by stickerset IDs                                                                  |

## Result

[Bool](https://core.telegram.org/type/Bool)

## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |

## Can bots use this method?

Yes

## Related pages