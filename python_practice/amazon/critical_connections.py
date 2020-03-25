""" Critical Connections
https://leetcode.com/problems/critical-connections-in-a-network/

Given an underected connected graph with n nodes labeled 1..n. 
A bridge (cut edge) is defined as an edge which, when removed, 
makes the graph disconnected (or more precisely, 
increases the number of connected components in the graph). 
Equivalently, an edge is a bridge if and only if it is not contained in any cycle. 
The task is to find all bridges in the given graph. 
Output an empty list if there are no bridges.

Input:
n, an int representing the total number of nodes.
edges, a list of pairs of integers representing the nodes connected by an edge.