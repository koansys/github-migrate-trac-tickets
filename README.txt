==============================
 GitHub: Migrate Trac Tickets
==============================

GitHub Issues API
=================

Offer a minimal API to work with GitHub's Issues via the v3 API.

It can GET issues, comments, labels, milestones, and can POST data to
create new ones via a simple dictionary.

Migrate Trac Tickets to GitHub Issues
=====================================

A sample program uses this to migrate Trac tickets into GitHub Issues.

It creates and merges "Milestones".

It uses Trac "Components" as GitHub "Labels".

It cannot migrate ticket ownership to GitHub Issue "Assignee" since we
have no way to map customer-specific Trac usernames into global GitHub
usernames.

