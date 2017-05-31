<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
  	<head>
  		<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />

		<!-- jQuery library -->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>

		<!-- Latest compiled JavaScript -->
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  	</head>
  <body>
  	<div class="container">
  		<div class="page-header">
	  		<h2 class="text-primary">My CD Collection</h2>
	  	</div>

<!-- 	  	<button type="button" class="btn btn-info" data-toggle="collapse" data-darget="#demo">Click me</button> -->

	  	<div class="table-responsive">
		    <table class="table table-hover">
		    	<thead>
					<tr>
				    	<th class="text-info">Title</th>
				    	<th class="text-info">Interpret name</th>
				    </tr>
				</thead>
				<tbody>
			    	<xsl:for-each select="catalog/cd">
			    		<xsl:choose>
			      			<xsl:when test="year = 1988">
			      				<tr class="info">
						       		<td><div class="text-uppercase text-success"><xsl:value-of select="title" /></div></td>
						       		<td><div class="text-uppercase text-success"><xsl:value-of select="artist" /></div></td>
					      		</tr>
			      			</xsl:when>
			      			<xsl:otherwise>
			      				<tr class="active">
						        	<td><div class="text-danger"><xsl:value-of select="title" /></div></td>
						        	<td><div class="text-danger"><xsl:value-of select="artist" /></div></td>
						      	</tr>
			      			</xsl:otherwise>
			      		</xsl:choose>
			      	</xsl:for-each>
			  	</tbody>
		    </table>
		</div>
	</div>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>


