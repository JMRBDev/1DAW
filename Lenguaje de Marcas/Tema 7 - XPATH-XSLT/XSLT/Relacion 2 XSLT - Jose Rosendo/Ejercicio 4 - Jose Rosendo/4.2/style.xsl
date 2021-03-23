<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>4.2 - Jose Rosendo</title>
                <style>
                    html {font-family: Arial, Helvetica, sans-serif;}
                    ul {list-style-type:none;}
                    li {color: black;}
                    .odd {background-color: #2fd8a6; color: white; font-size: 18px; font-weight: bold;}
                    .even {background-color: #d6d6d6; color: black; padding: 10 20; font-size: 12px; font-style: italic;}
                    .grey-li {background-color:#dbdbdb; font-size:14pt; color:blue;}
                </style>
            </head>
            <body>
                <h1>Relación 2 XSLT - Jose Rosendo</h1>
                <h2>Ejercicio 4.2</h2>
                <ul>
                    <xsl:for-each select="breakfast_menu/food">
                        <li class="grey-li">
                            <a href="#{@refid}">
                                <xsl:choose>
                                    <xsl:when test="id(@refid)/@xreftext">
                                        <xsl:value-of select="name"/>
                                    </xsl:when>
                                    <xsl:otherwise>
                                        <xsl:value-of select="name"/>
                                    </xsl:otherwise>
                                </xsl:choose>
                            </a>
                        </li>
                    </xsl:for-each>
                </ul>
                <xsl:for-each select="breakfast_menu/food">
                    <ul>
                        <li class="odd">
                            <a name="{@id}"/>
                            <xsl:value-of select="name"/>
 -                            <xsl:value-of select="price"/>
                        </li>
                        <li class="even">
                            <xsl:value-of select="description"/>
 per serving</li>
                    </ul>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>