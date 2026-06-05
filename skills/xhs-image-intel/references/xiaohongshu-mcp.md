# Xiaohongshu MCP Reference

Use this reference when the `xiaohongshu-mcp` MCP server is connected.

## Expected Server

Default HTTP MCP endpoint:

```text
http://localhost:18060/mcp
```

If the tool is not visible, search for MCP tools first. If unavailable, tell the user the MCP server must be running and connected before live Xiaohongshu collection can happen.

## Collection Tools

Use these read-only tools for this skill:

| Tool | Purpose | Notes |
| --- | --- | --- |
| `check_login_status` | Check whether the account is logged in | No parameters |
| `search_feeds` | Search notes by keyword | Requires `keyword`; accepts `filters` |
| `list_feeds` | Read homepage feed | Use only when the user asks for discovery without a keyword |
| `get_feed_detail` | Fetch note detail | Requires `feed_id` and `xsec_token` from search/list results |
| `user_profile` | Fetch public user profile | Use only if user/profile context is needed |

Avoid side-effect tools in this skill: `publish_content`, `publish_with_video`, `post_comment_to_feed`, `reply_comment_in_feed`, `like_feed`, `favorite_feed`, and `delete_cookies`.

## Search Filters

Pass filters only when needed:

```json
{
  "sort_by": "综合",
  "note_type": "图文",
  "publish_time": "不限",
  "search_scope": "不限",
  "location": "不限"
}
```

Allowed values commonly exposed by the server:

| Field | Values |
| --- | --- |
| `sort_by` | `综合`, `最新`, `最多点赞`, `最多评论`, `最多收藏` |
| `note_type` | `不限`, `视频`, `图文` |
| `publish_time` | `不限`, `一天内`, `一周内`, `半年内` |
| `search_scope` | `不限`, `已看过`, `未看过`, `已关注` |
| `location` | `不限`, `同城`, `附近` |

## Detail Options

Default detail request:

```json
{
  "feed_id": "<from search result>",
  "xsec_token": "<from search result>",
  "load_all_comments": false
}
```

Only set `load_all_comments=true` when comment analysis matters. Then keep a modest `limit`, such as `20`, and avoid aggressive scrolling.

## Data To Preserve

Keep these raw fields when present:

- `feed_id`, `xsec_token`, canonical URL
- title, description/body text
- author/user id, display name
- image URLs and cover image
- note type, publish time, location if present
- engagement counts: likes, favorites, comments, shares
- top comments when collected

Separate raw source fields from model-inferred image fields.
