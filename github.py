import base64
import json as simplejson
import urllib2

class GitHub(object):
    """Connections, queries and posts to GitHub.
    """
    def __init__(self, username, password, repo):
        """Username and password for auth; repo is like 'myorg/myapp'.
        """
        self.username = username
        self.password = password
        self.repo = repo
        self.url = "https://api.github.com/repos/%s" % self.repo
        self.auth = base64.encodestring('%s:%s' % (self.username, self.password))[:-1]

    def access(self, path, query=None, data=None):
        """Append the API path to the URL GET, or POST if there's data.
        """
        if not path.startswith('/'):
            path = '/' + path
        if query:
            path += '?' + query
        url = self.url + path
        req = urllib2.Request(url)
        req.add_header("Authorization", "Basic %s" % self.auth)
        try:
            if data:
                    req.add_header("Content-Type", "application/json")
                    res = urllib2.urlopen(req, simplejson.dumps(data))
            else:
                    res =  urllib2.urlopen(req)
            return simplejson.load(res)
        except (IOError, urllib2.HTTPError), e:
            raise RuntimeError("Error on url=%s e=%s" % (url, e))

    def issues(self, id_=None, query=None, data=None):
        """Get issues or POST and issue with data.
        Query for specifics like: issues(query='state=closed')
        Create a new one like:    issues(data={'title': 'Plough', 'body': 'Plover'})
        You ca NOT set the 'number' param and force a GitHub issue number.
        """
        path = 'issues'
        if id_:
            path += '/' + str(id_)
        return self.access(path, query=query, data=data)

    def issue_comments(self, id_, query=None, data=None):
        """Get comments for a ticket by its number or POST a comment with data.
        Example: issue_comments(5, data={'body': 'Is decapitated'})
        """
        # This call has no way to get a single comment
        #TODO: this is BROKEN
        return self.access('issues/%d/comments' % id_, query=query, data=data)

    def labels(self, query=None, data=None):
        """Get labels or POST a label with data.
        Post like: labels(data={'name': 'NewLabel'})
        """
        return self.access('labels', query=query, data=data)

    def milestones(self, query=None, data=None):
        """Get milestones or POST if data.
        Post like: milestones(data={'title':'NEWMILESTONE'})
        There are many other attrs you can set in the API.
        """
        return self.access('milestones', query=query, data=data)

