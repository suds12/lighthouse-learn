from django.db import models
from django.contrib import admin


class UserDp(models.Model):
    index = models.TextField(blank=True, null=True)
    values = models.FloatField(db_column='633', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'user_dp'


class LearningSet(models.Model):
    index = models.IntegerField(blank=True, null=False, primary_key=True)
    dataset = models.IntegerField(blank=True, null=True)
    package = models.IntegerField(blank=True, null=True)
    algorithm = models.IntegerField(blank=True, null=True)
    nvertices = models.IntegerField(blank=True, null=True)
    nedges = models.IntegerField(blank=True, null=True)
    nthreads = models.IntegerField(blank=True, null=True)
    nodes_in_largest_wcc = models.FloatField(db_column='Nodes.in.largest.WCC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    edges_in_largest_wcc = models.FloatField(db_column='Edges.in.largest.WCC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nodes_in_largest_scc = models.FloatField(db_column='Nodes.in.largest.SCC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    edges_in_largest_scc = models.FloatField(db_column='Edges.in.largest.SCC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    average_clustering_coefficient = models.FloatField(db_column='Average.clustering.coefficient', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_triangles = models.FloatField(db_column='Number.of.triangles', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fraction_of_closed_triangles = models.FloatField(db_column='Fraction.of.closed.triangles', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diameter_longest_shortest_path_field = models.FloatField(db_column='Diameter..longest.shortest.path.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    x90_percentile_effective_diameter = models.FloatField(db_column='X90.percentile.effective.diameter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    runtime = models.FloatField(blank=True, null=True)
    classif = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'learning_set'

class LearningSet1(models.Model):
    index = models.IntegerField(blank=True, null=False, primary_key=True)
    dataset = models.TextField(blank=True, null=True)
    package = models.TextField(blank=True, null=True)
    algorithm = models.TextField(blank=True, null=True)
    nvertices = models.IntegerField(blank=True, null=True)
    nedges = models.IntegerField(blank=True, null=True)
    nthreads = models.IntegerField(blank=True, null=True)
    nodes_in_largest_wcc = models.FloatField(db_column='Nodes.in.largest.WCC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    edges_in_largest_wcc = models.FloatField(db_column='Edges.in.largest.WCC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nodes_in_largest_scc = models.FloatField(db_column='Nodes.in.largest.SCC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    edges_in_largest_scc = models.FloatField(db_column='Edges.in.largest.SCC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    average_clustering_coefficient = models.FloatField(db_column='Average.clustering.coefficient', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_triangles = models.FloatField(db_column='Number.of.triangles', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fraction_of_closed_triangles = models.FloatField(db_column='Fraction.of.closed.triangles', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diameter_longest_shortest_path_field = models.FloatField(db_column='Diameter..longest.shortest.path.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    x90_percentile_effective_diameter = models.FloatField(db_column='X90.percentile.effective.diameter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    runtime = models.FloatField(blank=True, null=True)
    classif = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'learning_set1'


class Input(models.Model):
	dataset=models.TextField()

	class Meta:
		managed = False
		db_table = 'input-info'
