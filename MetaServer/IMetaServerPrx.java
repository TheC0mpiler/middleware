// **********************************************************************
//
// Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.7.0
//
// <auto-generated>
//
// Generated from file `meta-server.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package MetaServer;

public interface IMetaServerPrx extends com.zeroc.Ice.ObjectPrx
{
    default Song[] searchMusic(String name, String author, String album)
    {
        return searchMusic(name, author, album, com.zeroc.Ice.ObjectPrx.noExplicitContext);
    }

    default Song[] searchMusic(String name, String author, String album, java.util.Map<String, String> context)
    {
        return _iceI_searchMusicAsync(name, author, album, context, true).waitForResponse();
    }

    default java.util.concurrent.CompletableFuture<Song[]> searchMusicAsync(String name, String author, String album)
    {
        return _iceI_searchMusicAsync(name, author, album, com.zeroc.Ice.ObjectPrx.noExplicitContext, false);
    }

    default java.util.concurrent.CompletableFuture<Song[]> searchMusicAsync(String name, String author, String album, java.util.Map<String, String> context)
    {
        return _iceI_searchMusicAsync(name, author, album, context, false);
    }

    default com.zeroc.IceInternal.OutgoingAsync<Song[]> _iceI_searchMusicAsync(String iceP_name, String iceP_author, String iceP_album, java.util.Map<String, String> context, boolean sync)
    {
        com.zeroc.IceInternal.OutgoingAsync<Song[]> f = new com.zeroc.IceInternal.OutgoingAsync<>(this, "searchMusic", null, sync, null);
        f.invoke(true, context, null, ostr -> {
                     ostr.writeString(iceP_name);
                     ostr.writeString(iceP_author);
                     ostr.writeString(iceP_album);
                 }, istr -> {
                     Song[] ret;
                     ret = SongSeqHelper.read(istr);
                     return ret;
                 });
        return f;
    }

    default void connectToMe(String port)
    {
        connectToMe(port, com.zeroc.Ice.ObjectPrx.noExplicitContext);
    }

    default void connectToMe(String port, java.util.Map<String, String> context)
    {
        _iceI_connectToMeAsync(port, context, true).waitForResponse();
    }

    default java.util.concurrent.CompletableFuture<Void> connectToMeAsync(String port)
    {
        return _iceI_connectToMeAsync(port, com.zeroc.Ice.ObjectPrx.noExplicitContext, false);
    }

    default java.util.concurrent.CompletableFuture<Void> connectToMeAsync(String port, java.util.Map<String, String> context)
    {
        return _iceI_connectToMeAsync(port, context, false);
    }

    default com.zeroc.IceInternal.OutgoingAsync<Void> _iceI_connectToMeAsync(String iceP_port, java.util.Map<String, String> context, boolean sync)
    {
        com.zeroc.IceInternal.OutgoingAsync<Void> f = new com.zeroc.IceInternal.OutgoingAsync<>(this, "connectToMe", null, sync, null);
        f.invoke(false, context, null, ostr -> {
                     ostr.writeString(iceP_port);
                 }, null);
        return f;
    }

    default void deconnectMe(String port)
    {
        deconnectMe(port, com.zeroc.Ice.ObjectPrx.noExplicitContext);
    }

    default void deconnectMe(String port, java.util.Map<String, String> context)
    {
        _iceI_deconnectMeAsync(port, context, true).waitForResponse();
    }

    default java.util.concurrent.CompletableFuture<Void> deconnectMeAsync(String port)
    {
        return _iceI_deconnectMeAsync(port, com.zeroc.Ice.ObjectPrx.noExplicitContext, false);
    }

    default java.util.concurrent.CompletableFuture<Void> deconnectMeAsync(String port, java.util.Map<String, String> context)
    {
        return _iceI_deconnectMeAsync(port, context, false);
    }

    default com.zeroc.IceInternal.OutgoingAsync<Void> _iceI_deconnectMeAsync(String iceP_port, java.util.Map<String, String> context, boolean sync)
    {
        com.zeroc.IceInternal.OutgoingAsync<Void> f = new com.zeroc.IceInternal.OutgoingAsync<>(this, "deconnectMe", null, sync, null);
        f.invoke(false, context, null, ostr -> {
                     ostr.writeString(iceP_port);
                 }, null);
        return f;
    }

    /**
     * Contacts the remote server to verify that the object implements this type.
     * Raises a local exception if a communication error occurs.
     * @param obj The untyped proxy.
     * @return A proxy for this type, or null if the object does not support this type.
     **/
    static IMetaServerPrx checkedCast(com.zeroc.Ice.ObjectPrx obj)
    {
        return com.zeroc.Ice.ObjectPrx._checkedCast(obj, ice_staticId(), IMetaServerPrx.class, _IMetaServerPrxI.class);
    }

    /**
     * Contacts the remote server to verify that the object implements this type.
     * Raises a local exception if a communication error occurs.
     * @param obj The untyped proxy.
     * @param context The Context map to send with the invocation.
     * @return A proxy for this type, or null if the object does not support this type.
     **/
    static IMetaServerPrx checkedCast(com.zeroc.Ice.ObjectPrx obj, java.util.Map<String, String> context)
    {
        return com.zeroc.Ice.ObjectPrx._checkedCast(obj, context, ice_staticId(), IMetaServerPrx.class, _IMetaServerPrxI.class);
    }

    /**
     * Contacts the remote server to verify that a facet of the object implements this type.
     * Raises a local exception if a communication error occurs.
     * @param obj The untyped proxy.
     * @param facet The name of the desired facet.
     * @return A proxy for this type, or null if the object does not support this type.
     **/
    static IMetaServerPrx checkedCast(com.zeroc.Ice.ObjectPrx obj, String facet)
    {
        return com.zeroc.Ice.ObjectPrx._checkedCast(obj, facet, ice_staticId(), IMetaServerPrx.class, _IMetaServerPrxI.class);
    }

    /**
     * Contacts the remote server to verify that a facet of the object implements this type.
     * Raises a local exception if a communication error occurs.
     * @param obj The untyped proxy.
     * @param facet The name of the desired facet.
     * @param context The Context map to send with the invocation.
     * @return A proxy for this type, or null if the object does not support this type.
     **/
    static IMetaServerPrx checkedCast(com.zeroc.Ice.ObjectPrx obj, String facet, java.util.Map<String, String> context)
    {
        return com.zeroc.Ice.ObjectPrx._checkedCast(obj, facet, context, ice_staticId(), IMetaServerPrx.class, _IMetaServerPrxI.class);
    }

    /**
     * Downcasts the given proxy to this type without contacting the remote server.
     * @param obj The untyped proxy.
     * @return A proxy for this type.
     **/
    static IMetaServerPrx uncheckedCast(com.zeroc.Ice.ObjectPrx obj)
    {
        return com.zeroc.Ice.ObjectPrx._uncheckedCast(obj, IMetaServerPrx.class, _IMetaServerPrxI.class);
    }

    /**
     * Downcasts the given proxy to this type without contacting the remote server.
     * @param obj The untyped proxy.
     * @param facet The name of the desired facet.
     * @return A proxy for this type.
     **/
    static IMetaServerPrx uncheckedCast(com.zeroc.Ice.ObjectPrx obj, String facet)
    {
        return com.zeroc.Ice.ObjectPrx._uncheckedCast(obj, facet, IMetaServerPrx.class, _IMetaServerPrxI.class);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for the per-proxy context.
     * @param newContext The context for the new proxy.
     * @return A proxy with the specified per-proxy context.
     **/
    @Override
    default IMetaServerPrx ice_context(java.util.Map<String, String> newContext)
    {
        return (IMetaServerPrx)_ice_context(newContext);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for the adapter ID.
     * @param newAdapterId The adapter ID for the new proxy.
     * @return A proxy with the specified adapter ID.
     **/
    @Override
    default IMetaServerPrx ice_adapterId(String newAdapterId)
    {
        return (IMetaServerPrx)_ice_adapterId(newAdapterId);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for the endpoints.
     * @param newEndpoints The endpoints for the new proxy.
     * @return A proxy with the specified endpoints.
     **/
    @Override
    default IMetaServerPrx ice_endpoints(com.zeroc.Ice.Endpoint[] newEndpoints)
    {
        return (IMetaServerPrx)_ice_endpoints(newEndpoints);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for the locator cache timeout.
     * @param newTimeout The new locator cache timeout (in seconds).
     * @return A proxy with the specified locator cache timeout.
     **/
    @Override
    default IMetaServerPrx ice_locatorCacheTimeout(int newTimeout)
    {
        return (IMetaServerPrx)_ice_locatorCacheTimeout(newTimeout);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for the invocation timeout.
     * @param newTimeout The new invocation timeout (in seconds).
     * @return A proxy with the specified invocation timeout.
     **/
    @Override
    default IMetaServerPrx ice_invocationTimeout(int newTimeout)
    {
        return (IMetaServerPrx)_ice_invocationTimeout(newTimeout);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for connection caching.
     * @param newCache <code>true</code> if the new proxy should cache connections; <code>false</code> otherwise.
     * @return A proxy with the specified caching policy.
     **/
    @Override
    default IMetaServerPrx ice_connectionCached(boolean newCache)
    {
        return (IMetaServerPrx)_ice_connectionCached(newCache);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for the endpoint selection policy.
     * @param newType The new endpoint selection policy.
     * @return A proxy with the specified endpoint selection policy.
     **/
    @Override
    default IMetaServerPrx ice_endpointSelection(com.zeroc.Ice.EndpointSelectionType newType)
    {
        return (IMetaServerPrx)_ice_endpointSelection(newType);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for how it selects endpoints.
     * @param b If <code>b</code> is <code>true</code>, only endpoints that use a secure transport are
     * used by the new proxy. If <code>b</code> is false, the returned proxy uses both secure and
     * insecure endpoints.
     * @return A proxy with the specified selection policy.
     **/
    @Override
    default IMetaServerPrx ice_secure(boolean b)
    {
        return (IMetaServerPrx)_ice_secure(b);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for the encoding used to marshal parameters.
     * @param e The encoding version to use to marshal request parameters.
     * @return A proxy with the specified encoding version.
     **/
    @Override
    default IMetaServerPrx ice_encodingVersion(com.zeroc.Ice.EncodingVersion e)
    {
        return (IMetaServerPrx)_ice_encodingVersion(e);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for its endpoint selection policy.
     * @param b If <code>b</code> is <code>true</code>, the new proxy will use secure endpoints for invocations
     * and only use insecure endpoints if an invocation cannot be made via secure endpoints. If <code>b</code> is
     * <code>false</code>, the proxy prefers insecure endpoints to secure ones.
     * @return A proxy with the specified selection policy.
     **/
    @Override
    default IMetaServerPrx ice_preferSecure(boolean b)
    {
        return (IMetaServerPrx)_ice_preferSecure(b);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for the router.
     * @param router The router for the new proxy.
     * @return A proxy with the specified router.
     **/
    @Override
    default IMetaServerPrx ice_router(com.zeroc.Ice.RouterPrx router)
    {
        return (IMetaServerPrx)_ice_router(router);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for the locator.
     * @param locator The locator for the new proxy.
     * @return A proxy with the specified locator.
     **/
    @Override
    default IMetaServerPrx ice_locator(com.zeroc.Ice.LocatorPrx locator)
    {
        return (IMetaServerPrx)_ice_locator(locator);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for collocation optimization.
     * @param b <code>true</code> if the new proxy enables collocation optimization; <code>false</code> otherwise.
     * @return A proxy with the specified collocation optimization.
     **/
    @Override
    default IMetaServerPrx ice_collocationOptimized(boolean b)
    {
        return (IMetaServerPrx)_ice_collocationOptimized(b);
    }

    /**
     * Returns a proxy that is identical to this proxy, but uses twoway invocations.
     * @return A proxy that uses twoway invocations.
     **/
    @Override
    default IMetaServerPrx ice_twoway()
    {
        return (IMetaServerPrx)_ice_twoway();
    }

    /**
     * Returns a proxy that is identical to this proxy, but uses oneway invocations.
     * @return A proxy that uses oneway invocations.
     **/
    @Override
    default IMetaServerPrx ice_oneway()
    {
        return (IMetaServerPrx)_ice_oneway();
    }

    /**
     * Returns a proxy that is identical to this proxy, but uses batch oneway invocations.
     * @return A proxy that uses batch oneway invocations.
     **/
    @Override
    default IMetaServerPrx ice_batchOneway()
    {
        return (IMetaServerPrx)_ice_batchOneway();
    }

    /**
     * Returns a proxy that is identical to this proxy, but uses datagram invocations.
     * @return A proxy that uses datagram invocations.
     **/
    @Override
    default IMetaServerPrx ice_datagram()
    {
        return (IMetaServerPrx)_ice_datagram();
    }

    /**
     * Returns a proxy that is identical to this proxy, but uses batch datagram invocations.
     * @return A proxy that uses batch datagram invocations.
     **/
    @Override
    default IMetaServerPrx ice_batchDatagram()
    {
        return (IMetaServerPrx)_ice_batchDatagram();
    }

    /**
     * Returns a proxy that is identical to this proxy, except for compression.
     * @param co <code>true</code> enables compression for the new proxy; <code>false</code> disables compression.
     * @return A proxy with the specified compression setting.
     **/
    @Override
    default IMetaServerPrx ice_compress(boolean co)
    {
        return (IMetaServerPrx)_ice_compress(co);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for its connection timeout setting.
     * @param t The connection timeout for the proxy in milliseconds.
     * @return A proxy with the specified timeout.
     **/
    @Override
    default IMetaServerPrx ice_timeout(int t)
    {
        return (IMetaServerPrx)_ice_timeout(t);
    }

    /**
     * Returns a proxy that is identical to this proxy, except for its connection ID.
     * @param connectionId The connection ID for the new proxy. An empty string removes the connection ID.
     * @return A proxy with the specified connection ID.
     **/
    @Override
    default IMetaServerPrx ice_connectionId(String connectionId)
    {
        return (IMetaServerPrx)_ice_connectionId(connectionId);
    }

    static String ice_staticId()
    {
        return "::MetaServer::IMetaServer";
    }
}
